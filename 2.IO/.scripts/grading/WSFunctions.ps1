# =====================================================================
# CONFIGURATION
# =====================================================================
# Static IDs and flags used throughout participation grading
# =====================================================================

# LMS assignment ID where participation grades will be submitted
$LMSAssignmentID = 4

# Enables verbose/debug output when set to $true
$DEBUG = $false

# Explicit emoji → rubric level mapping for DB execution criterion
# (Used when the emoji represents more than pass/fail)
$EmojiToScore = @{
    ":grey_question:" = 18
    ":rocket:" = 19
    ":receipt:" = 21
    ":writing_hand:" = 23
    ":zero:" = 24
    ":one:" = 25
    ":asterisk:" = 25
}

# =====================================================================
# PARTICIPATION EXTRACTION FROM README.md
# =====================================================================

function Get-ParticipationGrades {
    <#
        Parses a Markdown table from a README.md file and converts
        emoji-based participation indicators into LMS rubric level IDs.

        Each valid row produces one grading entry keyed by Boréal ID.
    #>
    param (
        [Parameter(Mandatory)]
        [string]$Path
    )

    # Read README.md line-by-line
    $lines = Get-Content $Path
    $results = @()

    foreach ($line in $lines) {

        # Only process Markdown table rows starting with:
        # | <number> |
        if ($line -match '^\|\s*\d+\s*\|') {

            # Split on column separators
            $cols = $line -split '\|'

            # Column index reference (0 is empty due to leading pipe):
            # 1 = Row index
            # 2 = Boréal ID link
            # 5 = abacus emoji

            if ($DEBUG) { Write-Output $cols. }

            # Extract Boréal ID (expected format: [300000000])
            if ($cols[2] -match '\[(\d{9})\]') {
                $borealId = $matches[1]
            } else {
                # Skip malformed rows
                continue
            }

            # ---------------------------------
            # README.md quantity (fail/silver/gold)
            # ---------------------------------
            $readEmoji = ($cols[3]).Trim()
            $levels = @(13, 14, 15)  # fail, silver, gold
            $readScore = Get-RubricLevelIdFromReadmeEmoji `
                -Emoji $readEmoji `
                -Levels $levels

            # ---------------------------------
            # Images folder presence (pass/fail)
            # ---------------------------------
            $imgEmoji = ($cols[4]).Trim()
            $imgScore = Get-RubricLevelIdFromEmoji `
                -Emoji $imgEmoji `
                -FailLevelId 16 `
                -PassLevelId 17

            # If README.md exceeds expectations,
            # images folder is implicitly considered present
            if ($readScore -gt 15) {
                $imgScore = 17
            }

            # ---------------------------------
            # IO.py execution
            # ---------------------------------
            $ioEmoji = ($cols[5]).Trim()
            $ioScore = $EmojiToScore[$ioEmoji]

            # ---------------------------------
            # RAPPORT presence
            # ---------------------------------
            if ($cols[6] -match ':receipt:') {
                $receiptEmoji = ':receipt:'
                $receiptScore = $EmojiToScore[$receiptEmoji]            
            } else {
                $receiptEmoji = ':x:'
                receiptScore = 20
            }
            
            # ---------------------------------
            # Signature presence
            # ---------------------------------
            $sgnEmoji = ($cols[7]).Trim()
            if ($sgnEmoji -match ':writing_hand:') {
                $sgnScore = $EmojiToScore[$sgnEmoji]            
            } else {
                $sgnScore = 22
            }

            # ---------------------------------
            # Figure presence
            # ---------------------------------
            $figEmoji = ($cols[8]).Trim()
            if ($figEmoji -notmatch ':zero:|:one:') {
                $figEmoji = ':asterisk:'
            }
            $figScore = $EmojiToScore[$figEmoji]

            # ---------------------------------
            # etudiants.txt presence
            # ---------------------------------
            if ($cols[9] -match ':heavy_check_mark:') {
                $etuEmoji = ':heavy_check_mark:'
            } else {
                $etuEmoji = ':x:'
            }
            $etuScore = Get-RubricLevelIdFromEmoji `
                -Emoji $etuEmoji `
                -FailLevelId 26 `
                -PassLevelId 27

            # ---------------------------------
            # resultats.txt presence
            # ---------------------------------
            if ($cols[10] -match ':heavy_check_mark:') {
                $resEmoji = ':heavy_check_mark:'
            } else {
                $resEmoji = ':x:'
            }
            $resScore = Get-RubricLevelIdFromEmoji `
                -Emoji $resEmoji `
                -FailLevelId 28 `
                -PassLevelId 29

            # Debug trace for validation / troubleshooting
            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $ioEmoji, $ioScore
                    , $receiptEmoji, $receiptScore
                    , $etuEmoji, $etuScore
                    , $resEmoji, $resScore
            }

            # Accumulate normalized grading entry
            $results += [PSCustomObject]@{
                borealId  = $borealId
                readme    = $readScore
                image     = $imgScore
                io        = $ioScore
                rapport   = $receiptScore
                signature = $sgnScore
                figure    = $figScore
                etudiants = $etuScore
                resultat  = $resScore
            }
        }
    }

    return $results
}

# =====================================================================
# RUBRIC OBJECT BUILDER
# =====================================================================

function New-LMSRubricFromEntry {
    <#
        Converts a normalized participation entry into
        an LMS-compatible rubric payload.

        Designed to prevent invalid submissions that
        could crash Moodle grading APIs.
    #>
    param (
        [Parameter(Mandatory)]
        [object]$Entry
    )

    # Required grading components
    $requiredFields = @(
         "readme"
        , "image"
        , "io"
        , "rapport"
        , "signature"
        , "figure"
        , "etudiants"
        , "resultat"
    )

    # Validate entry completeness
    foreach ($field in $requiredFields) {
        if (-not $Entry.PSObject.Properties.Name -contains $field) {
            throw "Missing field '$field' in entry"
        }
    }

    # Construct rubric payload in LMS criterion order
    $rubric = @(
        @{ criterionid = 5;  levelid = $Entry.readme;    remark = "Quantité README.md " }
        @{ criterionid = 6;  levelid = $Entry.image;     remark = "présence répertoire images " }
        @{ criterionid = 7;  levelid = $Entry.io;        remark = "Éxécution de IO.py" }
        @{ criterionid = 8;  levelid = $Entry.rapport;   remark = "Présence Rapport Jupyter Notebook" }
        @{ criterionid = 9;  levelid = $Entry.signature; remark = "Présence Signature" }
        @{ criterionid = 10; levelid = $Entry.figure;    remark = "Nombre de Figures dans le rapport" }
        @{ criterionid = 11; levelid = $Entry.etudiants; remark = "Présence etudiants.txt" }
        @{ criterionid = 12; levelid = $Entry.resultat;  remark = "Présence resultat.txt" }
    )

    # Safety check: ensure all level IDs exist
    # (Null level IDs can cause Moodle submission failures)
    foreach ($r in $rubric) {
        if (-not $r.levelid) {
            throw "Invalid levelid for criterion $($r.criterionid)"
        }
    }

    return $rubric
}
# =====================================================================
# CONFIGURATION
# =====================================================================
# Static IDs and flags used throughout participation grading
# =====================================================================

# LMS assignment ID where participation grades will be submitted
$LMSAssignmentID = 18

# Enables verbose/debug output when set to $true
$DEBUG = $false

# Explicit emoji → rubric level mapping for DB execution criterion
# (Used when the emoji represents more than pass/fail)
$EmojiToScore = @{
    ":bangbang:" = 194
    ":rocket:" = 203
    ":receipt:" = 196
    ":writing_hand:" = 198
    ":zero:" = 200
    ":asterisk:" = 204
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
            $levels = @(188, 189, 190)  # fail, silver, gold
            $readScore = Get-RubricLevelIdFromReadmeEmoji `
                -Emoji $readEmoji `
                -Levels $levels

            # ---------------------------------
            # Images folder presence (pass/fail)
            # ---------------------------------
            $imgEmoji = ($cols[4]).Trim()
            $imgScore = Get-RubricLevelIdFromEmoji `
                -Emoji $imgEmoji `
                -FailLevelId 191 `
                -PassLevelId 192

            # If README.md exceeds expectations,
            # images folder is implicitly considered present
            if ($readScore -gt 190) {
                $imgScore = 192
            }

            # ---------------------------------
            # main.py execution
            # matches :rocket: :bangbang: 
            # if :x: revert to null‑coalescing operator (??) default value
            # ---------------------------------
            if ($cols[5] -match '(:[^:]+:)') {
                $mainEmoji = $matches[1]
                $mainScore = $EmojiToScore[$mainEmoji]  ?? 193
            }

            # ---------------------------------
            # RAPPORT presence
            # matches :receipt: 
            # if :x: or :boom: revert to null‑coalescing operator (??) default value
            # ---------------------------------
            if ($cols[6] -match '(:[^:]+:)') {
                $receiptEmoji = $matches[1]
                $receiptScore = $EmojiToScore[$receiptEmoji] ?? 195      
            }
            
            # ---------------------------------
            # Signature presence
            # ---------------------------------
            if ($cols[7] -match '(:[^:]+:)') {
                $sgnEmoji = $matches[1]
                $sgnScore = $EmojiToScore[$sgnEmoji] ?? 197
            }

            # ---------------------------------
            # Figure presence
            # ---------------------------------
            if ($cols[8] -match '(:[^:]+:)') {
                $figEmoji = $matches[1]

                # If emoji is NOT one of the allowed ones
                if ($figEmoji -notmatch '^:(zero|x|boom):$') {
                    $figEmoji = ':asterisk:'
                }

                $figScore = $EmojiToScore[$figEmoji] ?? 199
            }

            # ---------------------------------
            # requirements.txt presence
            # ---------------------------------
            if ($cols[9] -match '(:[^:]+:)') {
                $reqEmoji = $matches[1]
                $reqScore = Get-RubricLevelIdFromEmoji `
                    -Emoji $reqEmoji `
                    -FailLevelId 201 `
                    -PassLevelId 202
            }

            # Debug trace for validation / troubleshooting
            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $mainEmoji, $mainScore
                    , $receiptEmoji, $receiptScore
                    , $sgnEmoji, $sgnScore
                    , $figEmoji, $figScore
                    , $reqEmoji, $reqScore
            }

            # Accumulate normalized grading entry
            $results += [PSCustomObject]@{
                borealId  = $borealId
                readme    = $readScore
                image     = $imgScore
                main      = $mainScore
                rapport   = $receiptScore
                signature = $sgnScore
                figure    = $figScore
                req       = $reqScore
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
        , "main"
        , "rapport"
        , "signature"
        , "figure"
        , "req"
    )

    # Validate entry completeness
    foreach ($field in $requiredFields) {
        if (-not $Entry.PSObject.Properties.Name -contains $field) {
            throw "Missing field '$field' in entry"
        }
    }

    # Construct rubric payload in LMS criterion order
    $rubric = @(
        @{ criterionid = 82; levelid = $Entry.readme;    remark = "Quantité README.md " }
        @{ criterionid = 83; levelid = $Entry.image;     remark = "présence répertoire images " }
        @{ criterionid = 84; levelid = $Entry.main;      remark = "Éxécution de main.py" }
        @{ criterionid = 85; levelid = $Entry.rapport;   remark = "Présence Rapport Jupyter Notebook" }
        @{ criterionid = 86; levelid = $Entry.signature; remark = "Présence Signature" }
        @{ criterionid = 87; levelid = $Entry.figure;    remark = "Nombre de Figures dans le rapport" }
        @{ criterionid = 88; levelid = $Entry.req;       remark = "Présence requirements.txt" }
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
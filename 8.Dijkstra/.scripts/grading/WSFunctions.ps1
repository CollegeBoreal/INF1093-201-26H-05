# =====================================================================
# CONFIGURATION
# =====================================================================
# Static IDs and flags used throughout participation grading
# =====================================================================

# LMS assignment ID where participation grades will be submitted
$LMSAssignmentID = 19

# Enables verbose/debug output when set to $true
$DEBUG = $false

# Explicit emoji → rubric level mapping for DB execution criterion
# (Used when the emoji represents more than pass/fail)
$EmojiToScore = @{
    ":building_construction:" = 216
    ":checkered_flag:" = 211
    ":rocket:" = 212
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
            $levels = @(205, 206, 207)  # fail, silver, gold
            $readScore = Get-RubricLevelIdFromReadmeEmoji `
                -Emoji $readEmoji `
                -Levels $levels

            # ---------------------------------
            # Images folder presence (pass/fail)
            # ---------------------------------
            $imgEmoji = ($cols[4]).Trim()
            $imgScore = Get-RubricLevelIdFromEmoji `
                -Emoji $imgEmoji `
                -FailLevelId 208 `
                -PassLevelId 209

            # If README.md exceeds expectations,
            # images folder is implicitly considered present
            if ($readScore -gt 207) {
                $imgScore = 209
            }

            # ---------------------------------
            # Structure execution
            # matches :building_construction:
            # if :x: revert to null‑coalescing operator (??) default value
            # ---------------------------------
            if ($cols[5] -match '(:[^:]+:)') {
                $structureEmoji = $matches[1]
                $structureScore = $EmojiToScore[$structureEmoji]  ?? 215
            }

            # ---------------------------------
            # check_results presence
            # matches :checkered_flag: or :rocket:
            # if :x: or :boom: revert to null‑coalescing operator (??) default value
            # ---------------------------------
            if ($cols[6] -match '(:[^:]+:)') {
                $checkEmoji = $matches[1]
                $checkScore = $EmojiToScore[$checkEmoji] ?? 210      
            }
            
            # ---------------------------------
            # RAPPORT.ipynb presence
            # ---------------------------------
            if ($cols[7] -match '(:[^:]+:)') {
                $receiptEmoji = $matches[1]
                $receiptScore = Get-RubricLevelIdFromEmoji `
                    -Emoji $receiptEmoji `
                    -FailLevelId 213 `
                    -PassLevelId 214
            }

            # Debug trace for validation / troubleshooting
            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $structureEmoji, $structureScore
                    , $checkEmoji, $checkScore
                    , $receiptEmoji, $receiptScore
            }

            # Accumulate normalized grading entry
            $results += [PSCustomObject]@{
                borealId  = $borealId
                readme    = $readScore
                image     = $imgScore
                structure = $structureScore
                check     = $checkScore
                rapport   = $receiptScore
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
        , "structure"
        , "check"
        , "rapport"
    )

    # Validate entry completeness
    foreach ($field in $requiredFields) {
        if (-not $Entry.PSObject.Properties.Name -contains $field) {
            throw "Missing field '$field' in entry"
        }
    }

    # Construct rubric payload in LMS criterion order
    $rubric = @(
        @{ criterionid = 89; levelid = $Entry.readme;    remark = "Quantité README.md " }
        @{ criterionid = 90; levelid = $Entry.image;     remark = "présence répertoire images " }
        @{ criterionid = 93; levelid = $Entry.structure; remark = "Présence de la structure" }
        @{ criterionid = 91; levelid = $Entry.check;     remark = "Éxécution des tests" }
        @{ criterionid = 92; levelid = $Entry.rapport;   remark = "Présence Rapport Jupyter Notebook" }
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
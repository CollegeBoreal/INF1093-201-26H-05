# =====================================================================
# CONFIGURATION
# =====================================================================
# Static IDs and flags used throughout participation grading
# =====================================================================

# LMS assignment ID where participation grades will be submitted
$LMSAssignmentID = 17

# Enables verbose/debug output when set to $true
$DEBUG = $false

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
            # 3-4 = others

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
            $levels = @(173, 174, 175)  # fail, silver, gold
            $readScore = Get-RubricLevelIdFromReadmeEmoji `
                -Emoji $readEmoji `
                -Levels $levels

            # ---------------------------------
            # Images folder presence (pass/fail)
            # ---------------------------------
            $imgEmoji = ($cols[4]).Trim()
            $imgScore = Get-RubricLevelIdFromEmoji `
                -Emoji $imgEmoji `
                -FailLevelId 176 `
                -PassLevelId 177

            # If README.md exceeds expectations,
            # images folder is implicitly considered present
            if ($readScore -gt 175) {
                $imgScore = 177
            }

            # ---------------------------------
            # ex1 presence
            # ---------------------------------
            $ex1Emoji = ($cols[5]).Trim()
            $ex1Score = Get-RubricLevelIdFromEmoji `
                -Emoji $ex1Emoji `
                -FailLevelId 178 `
                -PassLevelId 179

            # ---------------------------------
            # ex2 presence
            # ---------------------------------
            $ex2Emoji = ($cols[6]).Trim()
            $ex2Score = Get-RubricLevelIdFromEmoji `
                -Emoji $ex2Emoji `
                -FailLevelId 180 `
                -PassLevelId 181

            # ---------------------------------
            # ex3 presence
            # ---------------------------------
            $ex3Emoji = ($cols[7]).Trim()
            $ex3Score = Get-RubricLevelIdFromEmoji `
                -Emoji $ex3Emoji `
                -FailLevelId 182 `
                -PassLevelId 183

            # ---------------------------------
            # ex4 presence
            # ---------------------------------
            $ex4Emoji = ($cols[8]).Trim()
            $ex4Score = Get-RubricLevelIdFromEmoji `
                -Emoji $ex4Emoji `
                -FailLevelId 184 `
                -PassLevelId 185

            # ---------------------------------
            # ex5 presence
            # ---------------------------------
            $ex5Emoji = ($cols[9]).Trim()
            $ex5Score = Get-RubricLevelIdFromEmoji `
                -Emoji $ex5Emoji `
                -FailLevelId 186 `
                -PassLevelId 187

                # Debug trace for validation / troubleshooting
            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $ex1Emoji, $ex1Score
                    , $ex2Emoji, $ex2Score
                    , $ex3Emoji, $ex3Score
                    , $ex4Emoji, $ex4Score
                    , $ex5Emoji, $ex5Score
            }

            # Accumulate normalized grading entry
            $results += [PSCustomObject]@{
                borealId  = $borealId
                readme    = $readScore
                image     = $imgScore
                ex1       = $ex1Score
                ex2       = $ex2Score
                ex3       = $ex3Score
                ex4       = $ex4Score
                ex5       = $ex5Score
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
        , "ex1"
        , "ex2"
        , "ex3"
        , "ex4"
        , "ex5"
    )

    # Validate entry completeness
    foreach ($field in $requiredFields) {
        if (-not $Entry.PSObject.Properties.Name -contains $field) {
            throw "Missing field '$field' in entry"
        }
    }

    # Construct rubric payload in LMS criterion order
    $rubric = @(
        @{ criterionid = 75;  levelid = $Entry.readme;    remark = "Quantité README.md " }
        @{ criterionid = 76;  levelid = $Entry.image;     remark = "Présence répertoire images " }
        @{ criterionid = 77;  levelid = $Entry.ex1;       remark = "Présence ex1" }
        @{ criterionid = 78;  levelid = $Entry.ex2;       remark = "Présence ex2" }
        @{ criterionid = 79;  levelid = $Entry.ex3;       remark = "Présence ex3" }
        @{ criterionid = 80;  levelid = $Entry.ex4;       remark = "Présence ex4" }
        @{ criterionid = 81;  levelid = $Entry.ex5;       remark = "Présence ex5" }
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

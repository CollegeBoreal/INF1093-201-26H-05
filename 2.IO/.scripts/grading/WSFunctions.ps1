# =========================
# CONFIG
# =========================
$LMSAssignmentID = 4
$DEBUG = $false

$EmojiToScore = @{
    ":x:" = 0
    ":heavy_check_mark:" = 1
    ":2nd_place_medal:" = 14
    ":1st_place_medal:" = 15
    ":grey_question:" = 18
    ":rocket:" = 19
    ":receipt:" = 21
    ":writing_hand:" = 23
    ":one:" = 25
    ":zero:" = 24
}

function Get-ParticipationGrades {
    param (
        [Parameter(Mandatory)]
        [string]$Path
    )

    $lines = Get-Content $Path
    $results = @()

    foreach ($line in $lines) {

        # Only data rows start with "| <number> |"
        if ($line -match '^\|\s*\d+\s*\|') {

            $cols = $line -split '\|'

            # Columns (0 is empty):
            # 1 = index
            # 2 = Boréal ID link column
            # 5 = abacus emoji

            if ($DEBUG) { Write-Output $cols. }

            # if ($cols.Count -lt 6) { continue }

            if ($cols[2] -match '(\d{9})') {
                $borealId = $matches[1]
            } else {
                continue
            }

            # "levels": { "id": 13, "score": 0 },
            #           { "id": 14, "score": 1 },
            #           { "id": 15, "score": 2 } 
            $readEmoji = ($cols[3]).Trim()
            if ($readEmoji -match ':x:') {
                $readScore = 13
            } else {
                $readScore = $EmojiToScore[$readEmoji]
            }

            # "levels": { "id": 16, "score": 0 },
            #           { "id": 17, "score": 1 },
            $imgEmoji = ($cols[4]).Trim()
            if ($imgEmoji -match ':x:') {
                $imgScore = 16
            } else {
                $imgScore = 17
            }

            # "levels": { "id": 18, "score": 0 },
            #           { "id": 19, "score": 1 },
            $ioEmoji = ($cols[5]).Trim()
            $ioScore = $EmojiToScore[$ioEmoji]

            # "levels": { "id": 20, "score": 0 },
            #           { "id": 21, "score": 1 },
            if ($cols[6] -match ':receipt:') {
                $receiptEmoji = ':receipt:'
                $receiptScore = $EmojiToScore[$receiptEmoji]            
            } else {
                $receiptEmoji = ':x:'
                $receiptScore = 20
            }
            
            # "levels": { "id": 22, "score": 0 },
            #           { "id": 23, "score": 1 },
            $sgnEmoji = ($cols[7]).Trim()
            if ($sgnEmoji -match ':writing_hand:') {
                $sgnScore = $EmojiToScore[$sgnEmoji]            
            } else {
                $sgnScore = 22
            }

            # "levels": { "id": 24, "score": 0 },
            #           { "id": 25, "score": 1 },
            $figEmoji = ($cols[8]).Trim()
            $figScore = $EmojiToScore[$figEmoji]

            # "levels": { "id": 26, "score": 0 },
            #           { "id": 27, "score": 1 },
            if ($cols[9] -match ':heavy_check_mark:') {
                $etuEmoji = ':heavy_check_mark:'
                $etuScore = 27
            } else {
                $etuEmoji = ':x:'
                $etuScore = 26
            }

            # "levels": { "id": 28, "score": 0 },
            #           { "id": 29, "score": 1 },
            if ($cols[10] -match ':heavy_check_mark:') {
                $resEmoji = ':heavy_check_mark:'
                $resScore = 29
            } else {
                $resEmoji = ':x:'
                $resScore = 28
            }

            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $ioEmoji, $ioScore
                    , $receiptEmoji, $receiptScore
                    , $etuEmoji, $etuScore
                    , $resEmoji, $resScore
            }

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

function New-LMSRubricFromEntry {
    param (
        [Parameter(Mandatory)]
        [object]$Entry
    )

    # Validate required fields exist
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

    foreach ($field in $requiredFields) {
        if (-not $Entry.PSObject.Properties.Name -contains $field) {
            throw "Missing field '$field' in entry"
        }
    }

    # Build rubric
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

    # Validate level IDs (avoid Moodle crash)
    foreach ($r in $rubric) {
        if (-not $r.levelid) {
            throw "Invalid levelid for criterion $($r.criterionid)"
        }
    }

    return $rubric
}

function Send-LMSRubricGrade {
    param (
        [Parameter(Mandatory)]
        [string]$LMS_URL,

        [Parameter(Mandatory)]
        [string]$TOKEN,

        [Parameter(Mandatory)]
        [int]$AssignmentId,

        [Parameter(Mandatory)]
        [int]$UserId,

        [Parameter(Mandatory)]
        [array]$Rubric,

        [int]$AttemptNumber = 0,

        [string]$WorkflowState = "graded"
    )

    # -------------------------
    # BUILD BASE PAYLOAD
    # -------------------------
    $body = @{
        wstoken            = $TOKEN
        wsfunction         = "local_gradesaver_save_grade"
        moodlewsrestformat = "json"
        assignmentid       = $AssignmentId
        userid             = $UserId
        attemptnumber      = $AttemptNumber
        workflowstate      = $WorkflowState
    }

    # -------------------------
    # ADD RUBRIC DYNAMICALLY
    # -------------------------
    for ($i = 0; $i -lt $Rubric.Count; $i++) {
        $entry = $Rubric[$i]

        if (-not $entry.criterionid -or -not $entry.levelid) {
            throw "Invalid rubric entry at index $i"
        }

        $body["rubric[criteria][$i][criterionid]"] = $entry.criterionid
        $body["rubric[criteria][$i][levelid]"]     = $entry.levelid
        $body["rubric[criteria][$i][remark]"]      = $entry.remark
    }

    if ($DEBUG) { $body | ConvertTo-Json -Depth 10 }

    # -------------------------
    # CALL MOODLE API
    # -------------------------
    try {
        $response = Invoke-RestMethod -Method Post `
            -Uri "https://$LMS_URL/webservice/rest/server.php" `
            -Body $body

        return $response
    }
    catch {
        throw "Moodle API call failed: $($_.Exception.Message)"
    }
}
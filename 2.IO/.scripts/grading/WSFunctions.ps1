# =========================
# CONFIG
# =========================
$LMS_URL = $env:LMS_URL
$TOKEN   = $env:API_SYNC_TOKEN

$assignmentId = 8
$userId       = 268

$EmojiToScore = @{
    ":x:" = 0
    ":2nd_place_medal:" = 1
    ":1st_place_medal:" = 2
    ":heavy_check_mark:" = 1
    ":grey_question:" = 0
    ":rocket:" = 1
    ":receipt:" = 1
    ":writing_hand:" = 1
    ":one:" = 1
    ":zero:" = 0
}

$DEBUG = $false

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

            $readEmoji = ($cols[3]).Trim()
            $readScore = $EmojiToScore[$readEmoji]

            $imgEmoji = ($cols[4]).Trim()
            $imgScore = $EmojiToScore[$imgEmoji]

            $ioEmoji = ($cols[5]).Trim()
            $ioScore = $EmojiToScore[$ioEmoji]

            if ($cols[6] -match ':receipt:') {
                $receiptEmoji = ':receipt:'
            } else {
                $receiptEmoji = ':x:'
            }
            $receiptScore = $EmojiToScore[$receiptEmoji]            

            $sgnEmoji = ($cols[7]).Trim()
            $sgnScore = $EmojiToScore[$sgnEmoji]

            $figEmoji = ($cols[8]).Trim()
            $figScore = $EmojiToScore[$figEmoji]

            if ($cols[9] -match ':heavy_check_mark:') {
                $etuEmoji = ':heavy_check_mark:'
            } else {
                $etuEmoji = ':x:'
            }
            $etuScore = $EmojiToScore[$etuEmoji]

            if ($cols[10] -match ':heavy_check_mark:') {
                $resEmoji = ':heavy_check_mark:'
            } else {
                $resEmoji = ':x:'
            }
            $resScore = $EmojiToScore[$resEmoji]

            if ($DEBUG) {
                Write-Output $borealId
                    , $readEmoji, $readScore
                    , $imgEmoji, $imgScore
                    , $ioEmoji, $ioScore
                    , $receiptEmoji, $receiptScore
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

        [int]$Grade = 0,

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
        grade              = $Grade
        attemptnumber      = $AttemptNumber
        workflowstate      = $WorkflowState
    }

    # -------------------------
    # ADD RUBRIC DYNAMICALLY
    # -------------------------
    for ($i = 0; $i -lt $Rubric.Count; $i++) {

        if (-not $Rubric[$i].criterionid -or -not $Rubric[$i].levelid) {
            throw "Invalid rubric entry at index $i"
        }

        $body["rubric[criteria][$i][criterionid]"] = $Rubric[$i].criterionid
        $body["rubric[criteria][$i][levelid]"]     = $Rubric[$i].levelid
        $body["rubric[criteria][$i][remark]"]      = $Rubric[$i].remark
    }

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
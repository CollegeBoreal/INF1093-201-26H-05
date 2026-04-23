$body = @{
    wstoken            = $env:API_SYNC_TOKEN
    wsfunction         = "local_gradesaver_save_grade"
    moodlewsrestformat = "json"
    assignmentid       = 1
    userid             = 268
    attemptnumber      = 0
    workflowstate      = "graded"

    "rubric[criteria][0][criterionid]" = 1
    "rubric[criteria][0][levelid]"     = 3
    "rubric[criteria][0][remark]"      = "Good work on README"

    "rubric[criteria][1][criterionid]" = 2
    "rubric[criteria][1][levelid]"     = 6
    "rubric[criteria][1][remark]"      = "Images are present"
}

$body | ConvertTo-Json -Depth 10

$response = Invoke-RestMethod -Method Post `
    -Uri "https://$($env:LMS_URL)/webservice/rest/server.php" `
    -Body $body

$response | ConvertTo-Json -Depth 10
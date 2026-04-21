$body = @{
    wstoken            = $env:API_SYNC_TOKEN
    wsfunction         = "local_gradesaver_save_grade"
    moodlewsrestformat = "json"
    assignmentid       = 4
    userid             = 268
    attemptnumber      = 0
    workflowstate      = "graded"

    "rubric[criteria][0][criterionid]" = 5
    "rubric[criteria][0][levelid]"     = 14
    "rubric[criteria][0][remark]"      = "Good README"

    "rubric[criteria][1][criterionid]" = 6
    "rubric[criteria][1][levelid]"     = 17
    "rubric[criteria][1][remark]"      = "Images present"

    "rubric[criteria][2][criterionid]" = 7
    "rubric[criteria][2][levelid]"     = 19
    "rubric[criteria][2][remark]"      = "IO script OK"

    "rubric[criteria][3][criterionid]" = 8
    "rubric[criteria][3][levelid]"     = 21
    "rubric[criteria][3][remark]"      = "Report complete"

    "rubric[criteria][4][criterionid]" = 9
    "rubric[criteria][4][levelid]"     = 22
    "rubric[criteria][4][remark]"      = "Signature OK"

    "rubric[criteria][5][criterionid]" = 10
    "rubric[criteria][5][levelid]"     = 25
    "rubric[criteria][5][remark]"      = "Figures included"

    "rubric[criteria][6][criterionid]" = 11
    "rubric[criteria][6][levelid]"     = 27
    "rubric[criteria][6][remark]"      = "Students file OK"

    "rubric[criteria][7][criterionid]" = 12
    "rubric[criteria][7][remark]"      = "Results file OK"
    "rubric[criteria][7][levelid]"     = 29
}

$body | ConvertTo-Json -Depth 10

$response = Invoke-RestMethod -Method Post `
    -Uri "https://$($env:LMS_URL)/webservice/rest/server.php" `
    -Body $body

$response | ConvertTo-Json -Depth 10
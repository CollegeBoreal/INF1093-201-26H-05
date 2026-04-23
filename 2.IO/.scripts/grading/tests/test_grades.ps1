. .scripts/grading/WSfunctions.ps1

$rubric = @(
    @{ criterionid = 5;  levelid = 15; remark = "---- Good README" }
    @{ criterionid = 6;  levelid = 17; remark = "---- Images present" }
    @{ criterionid = 7;  levelid = 19; remark = "---- IO script OK" }
    @{ criterionid = 8;  levelid = 21; remark = "---- Report complete" }
    @{ criterionid = 9;  levelid = 23; remark = "---- Signature OK" }
    @{ criterionid = 10; levelid = 25; remark = "---- Figures included" }
    @{ criterionid = 11; levelid = 27; remark = "---- Students file OK" }
    @{ criterionid = 12; levelid = 29; remark = "---- Results file OK" }
)

$response = Send-LMSRubricGrade `
    -LMS_URL $env:LMS_URL `
    -TOKEN $env:API_SYNC_TOKEN `
    -AssignmentId 4 `
    -UserId 268 `
    -Rubric $rubric

$response | ConvertTo-Json -Depth 10
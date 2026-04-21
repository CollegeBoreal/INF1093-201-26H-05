# Exit on error
$ErrorActionPreference = "Stop"

. ../.scripts/students.ps1
. ../.scripts/grading/functions.ps1

. .scripts/grading/WSfunctions.ps1

$responseLMS = Get-LMSGradableUsers -LMS_COURSE $LMS_COURSE
$LMSStudents = Get-LMSStudentInfo -LMSResponse $responseLMS

$participation = Get-ParticipationGrades -Path ./.scripts/Participation.md

# Write-Output $participation

foreach ($entry in $participation) {

    $moodleId = $LMSStudents[$entry.borealId].moodleId
    if ($DEBUG) { Write-Output $moodleId, $entry.borealId }

    $rubric = @(
    @{ criterionid = 5;  levelid = $entry.readme;    remark = "Good README" }
    @{ criterionid = 6;  levelid = $entry.image;     remark = "Images present" }
    @{ criterionid = 7;  levelid = $entry.io;        remark = "IO script OK" }
    @{ criterionid = 8;  levelid = $entry.rapport;   remark = "Report complete" }
    @{ criterionid = 9;  levelid = $entry.signature; remark = "Signature OK" }
    @{ criterionid = 10; levelid = $entry.figure;    remark = "Figures included" }
    @{ criterionid = 11; levelid = $entry.etudiants; remark = "Students file OK" }
    @{ criterionid = 12; levelid = $entry.resultat;  remark = "Results file OK" }
    )

    $response = Send-LMSRubricGrade `
        -LMS_URL $env:LMS_URL `
        -TOKEN $env:API_SYNC_TOKEN `
        -AssignmentId $DevoirID `
        -UserId $moodleId `
        -Rubric $rubric

    # $response | ConvertTo-Json -Depth 10
    Write-Output "--------------------------------------"
    Write-Output $response

}



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

    $rubric = New-LMSRubricFromEntry -Entry $entry

    $response = Send-LMSRubricGrade `
        -LMS_URL $env:LMS_URL `
        -TOKEN $env:API_SYNC_TOKEN `
        -AssignmentId $LMSAssignmentID `
        -UserId $moodleId `
        -Rubric $rubric

    Write-Output "--------------------------------------"
    Write-Output $response

}



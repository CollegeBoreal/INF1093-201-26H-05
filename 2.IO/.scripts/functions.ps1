#!/usr/bin/env pwsh

function Test-ItemExists {
    param(
        [string]$Path
    )

    if (Test-Path $Path) {
        return ":heavy_check_mark:"
    }

    return ":x:"
}

function Get-StudentPaths {
    param(
        [string]$StudentID
    )

    return @{
        README   = "$StudentID/README.md"
        Images   = "$StudentID/images"
        PY       = "$StudentID/IO.py"
        NB       = "$StudentID/RAPPORT.ipynb"
        IN       = "$StudentID/etudiants.txt"
        OUT      = "$StudentID/resultats.txt"
    }
}

function Get-StudentChecks {
    param(
        [hashtable]$Paths
    )

    return @{
        README = Test-CommonItemExists -Path $Paths.README -IsReadme
        Images = Test-CommonItemExists -Path $Paths.Images
        PY     = Test-ItemExists -Path $Paths.PY
        NB     = Test-ItemExists -Path $Paths.NB
        IN     = Test-ItemExists -Path $Paths.IN
        OUT    = Test-ItemExists -Path $Paths.OUT
    }
}

function Test-AllRequiredFilesPresent {
    param(
        [hashtable]$Checks
    )

    return (
        $Checks.README -eq ":heavy_check_mark:" -and
        $Checks.Images -eq ":heavy_check_mark:" -and
        $Checks.PY     -eq ":heavy_check_mark:" -and
        $Checks.NB     -eq ":heavy_check_mark:" -and
        $Checks.IN     -eq ":heavy_check_mark:" -and
        $Checks.OUT    -eq ":heavy_check_mark:"
    )
}

function Write-PresenceHeader {
    Write-Output ""
    Write-Output "## :a: Présence"
    Write-Output ""

    Write-Output "|:hash:| Boréal :id: | README.md | images | :rocket: IO.py | :receipt: RAPPORT | :writing_hand: Sgn | :framed_picture: Figures | etudiants.txt | resultats.txt | :boom: Erreurs |"
    Write-Output "|------|-------------|-----------|--------|----------------|-------------------|--------------------|--------------------------|---------------|---------------|----------------|"
}


function Write-StudentRow {
    param(
        [int]$Index,
        [string]$StudentID,
        [string]$GitHubLink,
        [hashtable]$Checks,
        [PSCustomObject]$Result,
        [string]$ReadmePath
    )

    Write-Output "| $Index | [$StudentID](../$ReadmePath) :point_right: $GitHubLink | $($Checks.README) | $($Checks.Images) | $($Result.IO_Exec) | [$($Result.Rapport)](../$StudentID/RAPPORT.ipynb) | $($Result.Signature) | $($Result.FiguresCount) | $($Checks.IN) | $($Checks.OUT) | $($Result.Errors) |"
}


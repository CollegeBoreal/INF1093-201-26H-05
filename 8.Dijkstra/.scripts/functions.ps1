#!/usr/bin/env pwsh

# ---------- Fonctions ----------
function Test-ExecuteScript {
    param(
        [string]$Path,
        [string]$Script
    )

    $scriptPath = Join-Path $Path $Script

    if (-not (Test-Path $scriptPath)) {
        return ":boom:"
    }

    try {
        $output = python3 $scriptPath 2>&1

        if ($LASTEXITCODE -eq 0 -and $output -match "✅ Bravo, le chemin est correct !") {
            return ":rocket:"
        }

        # option simple : succès si exit code = 0
        return ":checkered_flag:"
    }
    catch {
        return ":boom:"
    }
}

function Test-Structure {
    param(
        [string]$Path
    )

    $paths = @(
        "$Path/graph.py",
        "$Path/dijkstra_tp.py",
        "$Path/check_results.py"
    )

    foreach ($f in $paths) {
        if (-not (Test-Path $f)) {
            return ":x:"
        }
    }

    return ":building_construction:"
}

function Get-StudentPaths {
    param(
        [string]$StudentID
    )

    return @{
        README   = "$StudentID/README.md"
        Images   = "$StudentID/images"
        STRUCT   = "$StudentID/"
    }
}

function Get-StudentChecks {
    param(
        [hashtable]$Paths
    )

    return @{
        README        = Test-CommonItemExists -Path $Paths.README -IsReadme
        Images        = Test-CommonItemExists -Path $Paths.Images
        STRUCT        = Test-Structure        -Path $Paths.STRUCT
        TEST_SCRIPT   = Test-ExecuteScript    -Path $Paths.STRUCT -Script "check_results.py"
    }
}

function Test-AllRequiredFilesPresent {
    param(
        [hashtable]$Checks
    )

    $validReadmeValues = @(
        ":1st_place_medal:",
        ":2nd_place_medal:"
    )

    return (
        $Checks.README -in $validReadmeValues -and
        $Checks.Images -eq ":heavy_check_mark:" -and
        $Checks.STRUCT  -eq ":building_construction:" -and
        $Checks.TEST_SCRIPT -eq ":rocket:" -or ":checkered_flag:"
    )
}

function Write-PresenceHeader {
    Write-Output ""
    Write-Output "## :a: Présence"
    Write-Output ""

    Write-Output "|:hash:| Boréal :id: | README.md | images | Structure | check_results |"
    Write-Output "|------|-------------|-----------|--------|-----------|---------------|"
}


function Write-StudentRow {
    param(
        [int]$Index,
        [string]$StudentID,
        [string]$GitHubLink,
        [string]$ReadmePath,
        [hashtable]$Checks
    )

    Write-Output "| $Index | [$StudentID](../$ReadmePath) :point_right: $GitHubLink | $($Checks.README) | $($Checks.Images) | $($Checks.STRUCT) | $($Checks.TEST_SCRIPT) |"
}
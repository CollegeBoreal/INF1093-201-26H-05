#!/usr/bin/env pwsh

# ---------- Fonctions ----------
function Test-Structure {
    param(
        [string]$Path
    )

    $paths = @(
        "$Path/insertion/main.py",
        "$Path/insertion/entree_insertion.txt",
        "$Path/shell/main.py",
        "$Path/shell/entree_shell.txt",
        "$Path/quick/main.py",
        "$Path/quick/entree_quick.txt"
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
        README    = Test-CommonItemExists -Path $Paths.README -IsReadme
        Images    = Test-CommonItemExists -Path $Paths.Images
        STRUCT    = Test-Structure        -Path $Paths.STRUCT
    }
}

function Test-AllRequiredFilesPresent {
    param(
        [hashtable]$Checks
    )

    $validReadmeValues = @(
        ":heavy_check_mark:",
        ":1st_place_medal:",
        ":2nd_place_medal:",
        ":3rd_place_medal:"
    )

    return (
        $Checks.README -in $validReadmeValues -and
        $Checks.Images -eq ":heavy_check_mark:" -and
        $Checks.TRUCT  -eq ":building_construction:"
    )
}

function Write-PresenceHeader {
    Write-Output ""
    Write-Output "## :a: Présence"
    Write-Output ""

    Write-Output "|:hash:| Boréal :id: | README.md | images | Structure |"
    Write-Output "|------|-------------|-----------|--------|-----------|"
}


function Write-StudentRow {
    param(
        [int]$Index,
        [string]$StudentID,
        [string]$GitHubLink,
        [string]$ReadmePath,
        [hashtable]$Checks
    )

    Write-Output "| $Index | [$StudentID](../$ReadmePath) :point_right: $GitHubLink | $($Checks.README) | $($Checks.Images) | $($Checks.STRUCT) |"
}
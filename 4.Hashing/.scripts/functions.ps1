#!/usr/bin/env pwsh

function Test-ItemExists {
    param(
        [string]$Path,
        [switch]$CheckMermaid
    )

    if (-not (Test-Path $Path)) {
        return ":x:"
    }

    if (-not $CheckMermaid) {
        return ":heavy_check_mark:"
    }

    $content = Get-Content $Path -Raw

    # Check for mermaid block
    $hasMermaid = $content -match '```mermaid'

    # Check for Markdown image: ![alt](url)
    $hasMdImage = $content -match '!\[.*?\]\(.*?\)'

    # Check for HTML image: <img src="...">
    $hasHtmlImage = $content -match '<img\s+[^>]*src\s*=\s*["''][^"'']+["'']'

    if ($hasMermaid -or $hasMdImage -or $hasHtmlImage) {
        return ":compass:"
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
        MERMAID  = "$StudentID/README.md"
        EX1      = "$StudentID/ex1_hash.py"
        EX2      = "$StudentID/ex2_insert.py"
        EX3      = "$StudentID/ex3_search.py"
        EX4      = "$StudentID/ex4_dict.py"
        EX5      = "$StudentID/ex5_wordcount.py"
    }
}

function Get-StudentChecks {
    param(
        [hashtable]$Paths
    )

    return @{
        README    = Test-CommonItemExists -Path $Paths.README -IsReadme
        Images    = Test-CommonItemExists -Path $Paths.Images
        EX1       = Test-ItemExists -Path $Paths.EX1
        EX2       = Test-ItemExists -Path $Paths.EX2
        EX3       = Test-ItemExists -Path $Paths.EX3
        EX4       = Test-ItemExists -Path $Paths.EX4
        EX5       = Test-ItemExists -Path $Paths.EX5
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
        $Checks.EX1    -eq ":heavy_check_mark:" -and
        $Checks.EX2    -eq ":heavy_check_mark:" -and
        $Checks.EX3    -eq ":heavy_check_mark:" -and
        $Checks.EX4    -eq ":heavy_check_mark:" -and
        $Checks.EX5    -eq ":heavy_check_mark:"
    )
}

function Write-PresenceHeader {
    Write-Output ""
    Write-Output "## :a: Présence"
    Write-Output ""

    Write-Output "|:hash:| Boréal :id: | README.md | images | ex1  | ex2 | ex3 | ex4 | ex5 |"
    Write-Output "|------|-------------|-----------|--------|------|-----|-----|-----|-----|"
}


function Write-StudentRow {
    param(
        [int]$Index,
        [string]$StudentID,
        [string]$GitHubLink,
        [string]$ReadmePath,
        [hashtable]$Checks
    )

    Write-Output "| $Index | [$StudentID](../$ReadmePath) :point_right: $GitHubLink | $($Checks.README) | $($Checks.Images) | $($Checks.EX1) | $($Checks.EX2) | $($Checks.EX3) | $($Checks.EX4) | $($Checks.EX5) |"
}


#requires -Version 5.1
<#
Upload full AI course collection (110 files) into a separate directory of
samiabo75/Data-Science-ML-Course. Run on Windows with Git installed and authenticated.
Usage:
powershell -ExecutionPolicy Bypass -File .\UPLOAD_FULL_COLLECTION.ps1 -ZipPath "C:\Downloads\AI_Course_2026_All_3_Libraries.zip"
Optional: -RepoPath "C:\path\to\Data-Science-ML-Course"
#>
param(
    [Parameter(Mandatory=$true)][string]$ZipPath,
    [string]$RepoPath = ""
)
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$RepoUrl = "https://github.com/samiabo75/Data-Science-ML-Course.git"
$Destination = "AI-Course-Textbooks-2026\ספרי_הקורס"
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git was not found. Install Git for Windows or GitHub Desktop with Git available in PATH."
}
$ZipPath = (Resolve-Path -LiteralPath $ZipPath).Path
$workspace = Join-Path $env:TEMP ("ai_course_upload_" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $workspace -Force | Out-Null
try {
    Expand-Archive -LiteralPath $ZipPath -DestinationPath $workspace -Force
    $source = Join-Path $workspace "AI_Course_Organized_2026"
    if (-not (Test-Path -LiteralPath $source)) { throw "ZIP missing AI_Course_Organized_2026 root folder" }
    $files = @(Get-ChildItem -LiteralPath $source -File -Recurse)
    if ($files.Count -ne 110) { throw "Unexpected file count $($files.Count), expected 110" }
    foreach ($f in $files) {
        if ($f.Length -ge 100MB) { throw "File over GitHub 100MB limit: $($f.FullName)" }
    }
    if ([string]::IsNullOrWhiteSpace($RepoPath)) {
        $RepoPath = Join-Path (Get-Location).Path "Data-Science-ML-Course"
        if (-not (Test-Path (Join-Path $RepoPath ".git"))) {
            git clone $RepoUrl $RepoPath
            if ($LASTEXITCODE -ne 0) { throw "git clone failed; authenticate with GitHub first" }
        }
    }
    $RepoPath = (Resolve-Path -LiteralPath $RepoPath).Path
    if (-not (Test-Path -LiteralPath (Join-Path $RepoPath ".git"))) { throw "RepoPath must be a Git repository" }
    $origin = (git -C $RepoPath remote get-url origin)
    if ($LASTEXITCODE -ne 0 -or ($origin -notmatch "samiabo75/Data-Science-ML-Course(\.git)?$")) {
        throw "Wrong git origin; refusing to push into unrelated repository: $origin"
    }
    $dirty = @(git -C $RepoPath status --porcelain)
    if ($dirty.Count -gt 0) { throw "Local repository has uncommitted changes. Commit/stash them first." }
    git -C $RepoPath checkout main
    if ($LASTEXITCODE -ne 0) { throw "Cannot check out main" }
    git -C $RepoPath pull --ff-only origin main
    if ($LASTEXITCODE -ne 0) { throw "Cannot fast-forward main. Resolve git divergence before upload." }
    $target = Join-Path $RepoPath $Destination
    if (Test-Path -LiteralPath $target) {
        throw "Target folder exists. Nothing was overwritten: $target"
    }
    New-Item -ItemType Directory -Path (Split-Path $target -Parent) -Force | Out-Null
    Copy-Item -LiteralPath $source -Destination $target -Recurse
    $copied = @(Get-ChildItem -LiteralPath $target -File -Recurse)
    if ($copied.Count -ne $files.Count) { throw "File count mismatch after copying" }
    git -C $RepoPath add -- "AI-Course-Textbooks-2026/ספרי_הקורס"
    if ($LASTEXITCODE -ne 0) { throw "git add failed" }
    git -C $RepoPath commit -m "Add complete AI course textbooks, 32 chapter labs and source PDFs"
    if ($LASTEXITCODE -ne 0) { throw "git commit failed" }
    git -C $RepoPath push origin main
    if ($LASTEXITCODE -ne 0) { throw "git push failed; local commit exists; check credentials / branch rules" }
    Write-Host "SUCCESS: Uploaded all $($files.Count) files to $Destination on main." -ForegroundColor Green
    Write-Host "https://github.com/samiabo75/Data-Science-ML-Course/tree/main/AI-Course-Textbooks-2026"
}
finally {
    if (Test-Path -LiteralPath $workspace) { Remove-Item -LiteralPath $workspace -Force -Recurse }
}

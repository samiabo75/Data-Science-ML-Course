# Windows PowerShell 5.1 compatible; ASCII-only source file.
# This script uploads the 110 course files from the ZIP without changing old course folders.
# Example (run inside Downloads):
# powershell -ExecutionPolicy Bypass -File ".\UPLOAD_FULL_COLLECTION.ps1" -ZipPath ".\AI_Course_2026_All_3_Libraries.zip"
param(
    [Parameter(Mandatory=$true)][string]$ZipPath,
    [string]$RepoPath = ""
)
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repoUrl = "https://github.com/samiabo75/Data-Science-ML-Course.git"
$gitFolder = "AI-Course-Textbooks-2026/Course-Libraries"
$requiredFileCount = 110

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is missing. Install Git for Windows and reopen PowerShell."
}
$zipFullPath = (Resolve-Path -LiteralPath $ZipPath).Path
$tempFolder = Join-Path $env:TEMP ("ai_course_" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $tempFolder -Force | Out-Null
try {
    Write-Host "Extracting ZIP..."
    Expand-Archive -LiteralPath $zipFullPath -DestinationPath $tempFolder -Force
    $source = Join-Path $tempFolder "AI_Course_Organized_2026"
    if (-not (Test-Path -LiteralPath $source -PathType Container)) {
        throw "ZIP is missing AI_Course_Organized_2026 directory."
    }

    $original = @(Get-ChildItem -LiteralPath $source -Recurse -File)
    if ($original.Count -ne $requiredFileCount) {
        throw "Wrong ZIP contents: found $($original.Count) files, expected $requiredFileCount."
    }
    foreach ($file in $original) {
        if ($file.Length -ge 100MB) {
            throw "File exceeds GitHub 100 MB limit: $($file.Name)"
        }
    }

    if ([string]::IsNullOrWhiteSpace($RepoPath)) {
        $RepoPath = Join-Path (Get-Location).Path "Data-Science-ML-Course"
        if (-not (Test-Path -LiteralPath (Join-Path $RepoPath ".git"))) {
            Write-Host "Cloning GitHub repository..."
            & git clone $repoUrl $RepoPath
            if ($LASTEXITCODE -ne 0) { throw "git clone failed." }
        }
    }
    $RepoPath = (Resolve-Path -LiteralPath $RepoPath).Path
    if (-not (Test-Path -LiteralPath (Join-Path $RepoPath ".git"))) {
        throw "RepoPath is not a Git repository."
    }
    $origin = (& git -C $RepoPath remote get-url origin)
    if ($LASTEXITCODE -ne 0 -or $origin -notmatch '(?i)github\.com[:/]samiabo75/Data-Science-ML-Course(\.git)?$') {
        throw "Unexpected remote repository: $origin"
    }
    $dirty = @(& git -C $RepoPath status --porcelain)
    if ($LASTEXITCODE -ne 0 -or $dirty.Count -gt 0) {
        throw "Git working directory has uncommitted changes. Commit or stash first."
    }

    & git -C $RepoPath checkout main
    if ($LASTEXITCODE -ne 0) { throw "Cannot checkout main." }
    & git -C $RepoPath pull --ff-only origin main
    if ($LASTEXITCODE -ne 0) { throw "Git pull failed. Resolve it before retrying." }

    $destination = Join-Path $RepoPath ($gitFolder.Replace("/", [string][IO.Path]::DirectorySeparatorChar))
    if (Test-Path -LiteralPath $destination) {
        throw "Destination already exists. No files overwritten: $destination"
    }

    Write-Host "Copying course libraries into repository..."
    New-Item -ItemType Directory -Path $destination -Force | Out-Null
    Get-ChildItem -LiteralPath $source -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $destination -Recurse -Force
    }
    $copied = @(Get-ChildItem -LiteralPath $destination -Recurse -File)
    if ($copied.Count -ne $requiredFileCount) {
        throw "Copy verification failed: $($copied.Count) files instead of $requiredFileCount."
    }
    & git -C $RepoPath add -- $gitFolder
    if ($LASTEXITCODE -ne 0) { throw "git add failed." }
    & git -C $RepoPath commit -m "Add complete AI textbooks: 32 chapters and labs"
    if ($LASTEXITCODE -ne 0) { throw "git commit failed. Configure git user.name/user.email if needed." }
    Write-Host "Pushing commit to GitHub..."
    & git -C $RepoPath push origin main
    if ($LASTEXITCODE -ne 0) {
        throw "git push failed. Commit is saved locally; check GitHub authentication."
    }
    Write-Host "SUCCESS: Uploaded 110 course files to GitHub." -ForegroundColor Green
    Write-Host "https://github.com/samiabo75/Data-Science-ML-Course/tree/main/AI-Course-Textbooks-2026/Course-Libraries"
}
finally {
    if (Test-Path -LiteralPath $tempFolder) {
        Remove-Item -LiteralPath $tempFolder -Recurse -Force
    }
}

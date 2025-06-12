param (
    [string]$FolderName,
    [double]$FrameRate,
    [int]$UsePng = 0  # Optional third argument (defaults to 0)
)

# Resolve absolute folder paths
$FullFolderPath = (Resolve-Path $FolderName).Path
$ParentFolderPath = (Get-Item $FullFolderPath).Parent.FullName

# Validate folder existence
if (-Not (Test-Path $FolderName -PathType Container)) {
    Write-Host "❌ Error: Folder '$FolderName' does not exist."
    exit 1
}

# Validate framerate
if ($FrameRate -le 0) {
    Write-Host "❌ Error: Framerate must be a positive number."
    exit 1
}

# Determine file pattern based on third argument
$FilePattern = "%03d.jpg"  # Default to JPG
if ($UsePng -eq 1) {
    $FilePattern = "%03d.png"  # Use PNG if third argument is 1
}

Write-Host "📷 Using file pattern: $FilePattern"

# Store the current directory
$OriginalDir = Get-Location

# Change to the target directory
Set-Location $FullFolderPath

# Define output filenames
$OutputFile = "slideshow.mp4"  # Temporary name inside folder
$FinalOutputFile = "`"$ParentFolderPath\$FolderName.mp4`""  # Moved to parent dir

# Run ffmpeg using Start-Process
Write-Host "🎥 Creating slideshow in '$FullFolderPath' at $FrameRate FPS..."
Start-Process -NoNewWindow -Wait -FilePath "ffmpeg" -ArgumentList `
    "-framerate $FrameRate -i `"$FilePattern`" -vf `"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2`" -c:v libx264 `"$FolderName`".mp4" -PassThru

# Move the output video to the parent directory
if (Test-Path $OutputFile) {
    Move-Item -Path $OutputFile -Destination $FinalOutputFile -Force
    Write-Host "✅ Slideshow created and moved to: $FinalOutputFile"
} else {
    Write-Host "❌ Error: ffmpeg did not generate the expected output file."
}

# Return to the parent directory
Set-Location $ParentFolderPath
Write-Host "↩ Returned to parent directory: $ParentFolderPath"

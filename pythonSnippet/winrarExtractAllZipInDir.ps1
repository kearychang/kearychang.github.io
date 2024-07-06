Get-ChildItem -Filter *.cbz | ForEach-Object {
    $folderName = $_.BaseName
    $extractPath = Join-Path (Get-Location) $folderName
    New-Item -Path $extractPath -ItemType Directory -Force | Out-Null
    & "C:\Program Files\WinRAR\WinRAR.exe" x $_.FullName $extractPath\
    $counter = 1
    Get-ChildItem -Path $extractPath | ForEach-Object {
        $newName = "{0}_{1:D3}{2}" -f $folderName, $counter, $_.Extension
        Rename-Item $_.FullName -NewName $newName
        $counter++
    }
}

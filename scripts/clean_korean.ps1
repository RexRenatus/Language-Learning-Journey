# Clean Korean-only rows and strip quotes in CSV chunks
$ErrorActionPreference = 'Stop'

$srcDir = "chunks_10k"
$dstDir = "chunks_10k_korean_clean"
$pattern = "Korean Ngram list_part_*.csv"

$regexKorean = '[\uAC00-\uD7A3\u1100-\u11FF\u3130-\u318F]'
$regexEnglish = '[A-Za-z]'

if (-not (Test-Path -LiteralPath $dstDir)) { New-Item -ItemType Directory -Path $dstDir | Out-Null }

$files = Get-ChildItem -LiteralPath $srcDir -Filter $pattern | Sort-Object Name
if (-not $files) { throw "No source chunk files found in $srcDir" }

$report = New-Object System.Collections.Generic.List[object]

foreach ($f in $files) {
    $inPath = $f.FullName
    $outPath = Join-Path $dstDir $f.Name

    $linesRead = 0
    $kept = 0
    $dropped = 0

    $sr = [System.IO.StreamReader]::new($inPath, [System.Text.Encoding]::UTF8)
    try {
        $headerLine = $sr.ReadLine()
        if ($null -eq $headerLine) { continue }

        $headerObj = $null
        try { $headerObj = ConvertFrom-Csv -InputObject $headerLine | Select-Object -First 1 } catch {}
        if ($headerObj) {
            $headers = @($headerObj.PSObject.Properties.Name)
        } else {
            $headers = @($headerLine.Trim('"') -split '\s*,\s*')
        }
        if (-not $headers -or $headers.Count -eq 0) { continue }

        $firstCol = $headers[0]

        $sw = [System.IO.StreamWriter]::new($outPath, $false, [System.Text.Encoding]::UTF8)
        try {
            $sw.WriteLine([string]::Join(',', $headers))
            while (($line = $sr.ReadLine()) -ne $null) {
                $linesRead++
                $obj = $null
                try {
                    $obj = ConvertFrom-Csv -InputObject ($headerLine + [Environment]::NewLine + $line) | Select-Object -First 1
                } catch {}
                if ($null -eq $obj) { $dropped++; continue }

                $val = [string]$obj.$firstCol
                if ($val -match $regexKorean -and $val -notmatch $regexEnglish) {
                    $vals = foreach ($h in $headers) {
                        $v = [string]$obj.$h
                        if ($null -eq $v) { '' } else { ($v -replace '"','') }
                    }
                    $sw.WriteLine([string]::Join(',', $vals))
                    $kept++
                } else {
                    $dropped++
                }
            }
        } finally {
            $sw.Dispose()
        }
    } finally {
        $sr.Dispose()
    }

    $report.Add([PSCustomObject]@{
        File    = $f.Name
        Checked = $linesRead
        Kept    = $kept
        Dropped = $dropped
    })
}

# Write clean_report.csv without quotes
$reportPath = Join-Path $dstDir 'clean_report.csv'
$wr = [System.IO.StreamWriter]::new($reportPath, $false, [System.Text.Encoding]::UTF8)
try {
    $wr.WriteLine('File,Checked,Kept,Dropped')
    foreach ($row in $report | Sort-Object File) {
        $wr.WriteLine(('{0},{1},{2},{3}' -f $row.File, $row.Checked, $row.Kept, $row.Dropped))
    }
} finally {
    $wr.Dispose()
}

# Validation: check data rows (exclude header) for ASCII letters and quotes
$englishViolations = New-Object System.Collections.Generic.List[string]
$quoteViolations = New-Object System.Collections.Generic.List[string]

foreach ($f in (Get-ChildItem -LiteralPath $dstDir -Filter $pattern | Sort-Object Name)) {
    $lines = Get-Content -LiteralPath $f.FullName
    if ($lines.Count -gt 1) {
        $data = $lines[1..($lines.Count-1)]
        if ($data | Select-String -Pattern $regexEnglish -Quiet) { $englishViolations.Add($f.Name) }
        if ($data | Select-String -Pattern '"' -Quiet) { $quoteViolations.Add($f.Name) }
    }
}

$summaryPath = Join-Path $dstDir 'validation_summary.txt'
$tw = [System.IO.StreamWriter]::new($summaryPath, $false, [System.Text.Encoding]::UTF8)
try {
    $tw.WriteLine("Cleaned files directory: $dstDir")
    $tw.WriteLine("Files processed: " + $files.Count)
    $tw.WriteLine("Report: " + $reportPath)
    if ($englishViolations.Count -gt 0) {
        $tw.WriteLine("Files with English letters in data rows: " + ($englishViolations -join ', '))
    } else {
        $tw.WriteLine("No English letters detected in data rows.")
    }
    if ($quoteViolations.Count -gt 0) {
        $tw.WriteLine('Files containing quotes in data rows: ' + ($quoteViolations -join ', '))
    } else {
        $tw.WriteLine('No quotes detected in data rows.')
    }
} finally {
    $tw.Dispose()
}

Write-Host ("Clean complete. Report: {0}; Summary: {1}" -f $reportPath, $summaryPath)
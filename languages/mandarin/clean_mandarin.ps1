$inputFile = "languages/mandarin/ngrams/Mandarin_Ngrams.csv"
$outputFile = "languages/mandarin/ngrams/clean/Mandarin_Ngrams_clean.csv"

Import-Csv $inputFile | ForEach-Object {
    $_.Item = $_.Item -replace '"', ''
    $_
} | Export-Csv -Path $outputFile -NoTypeInformation -Encoding UTF8
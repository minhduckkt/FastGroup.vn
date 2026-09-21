param(
  [switch]$Apply
)

$ErrorActionPreference = "Stop"

$toolDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $toolDir "..\..")
$portalRoot = Join-Path $repoRoot "rosemount-emerson-viet-nam"
$blogCssHref = "/rosemount-emerson-viet-nam/blog/assets/css/style.css"
$siteCssPattern = "/rosemount-emerson-viet-nam/assets/site.css"
$notoLink = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600;700&display=swap">'

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$htmlFiles = Get-ChildItem -Path $portalRoot -Recurse -Filter "index.html" -File
$stylePath = Join-Path $portalRoot "blog\assets\css\style.css"

$checked = 0
$blogPages = 0
$changed = 0
$remainingIssues = New-Object System.Collections.Generic.List[string]

foreach ($file in $htmlFiles) {
  $checked++
  $path = $file.FullName
  $html = [System.IO.File]::ReadAllText($path)
  $isBlogPage = $html.Contains($blogCssHref) -or $html.Contains("blog/assets/css/style.css") -or $html.Contains("Inter:wght")

  if (-not $isBlogPage) {
    continue
  }

  $blogPages++
  $newHtml = $html

  $newHtml = [regex]::Replace(
    $newHtml,
    '<link\s+href="https://fonts\.googleapis\.com/css2\?family=Inter:wght@400\.\.800&display=swap"\s+rel="stylesheet"\s*/?>',
    $notoLink,
    [System.Text.RegularExpressions.RegexOptions]::IgnoreCase
  )

  $newHtml = [regex]::Replace(
    $newHtml,
    '<link\s+rel="stylesheet"\s+href="https://fonts\.googleapis\.com/css2\?family=Inter:wght@400\.\.800&display=swap"\s*/?>',
    $notoLink,
    [System.Text.RegularExpressions.RegexOptions]::IgnoreCase
  )

  if ($newHtml -ne $html) {
    $changed++
    if ($Apply) {
      [System.IO.File]::WriteAllText($path, $newHtml, $utf8NoBom)
    }
    Write-Host ("{0}: font import -> Noto Sans" -f ($path.Substring($repoRoot.Path.Length + 1)))
  }

  if ($newHtml.Contains("Inter:wght")) {
    $remainingIssues.Add("Inter import remains: " + $path.Substring($repoRoot.Path.Length + 1))
  }
  if (-not $newHtml.Contains($siteCssPattern)) {
    $remainingIssues.Add("Missing portal site.css: " + $path.Substring($repoRoot.Path.Length + 1))
  }
  if (-not ($newHtml.Contains($blogCssHref) -or $newHtml.Contains("blog/assets/css/style.css"))) {
    $remainingIssues.Add("Missing blog style.css: " + $path.Substring($repoRoot.Path.Length + 1))
  }
}

Write-Host ""
Write-Host ("Checked HTML files : {0}" -f $checked)
Write-Host ("Blog pages found   : {0}" -f $blogPages)
Write-Host ("Pages changed      : {0}" -f $changed)
Write-Host ("Mode               : {0}" -f ($(if ($Apply) { "APPLY" } else { "CHECK ONLY" })))

if ($remainingIssues.Count -gt 0) {
  Write-Host ""
  Write-Host "Remaining issues:"
  foreach ($issue in $remainingIssues) {
    Write-Host ("- {0}" -f $issue)
  }
  exit 2
}

if (Test-Path $stylePath) {
  $styleCss = [System.IO.File]::ReadAllText($stylePath)
  if ($styleCss.Contains("Inter")) {
    Write-Host ""
    Write-Host "Remaining issues:"
    Write-Host ("- Blog CSS still references Inter: {0}" -f ($stylePath.Substring($repoRoot.Path.Length + 1)))
    exit 2
  }
  if (-not $styleCss.Contains("Fast Group alignment patch")) {
    Write-Host ""
    Write-Host "Remaining issues:"
    Write-Host ("- Blog CSS alignment patch marker missing: {0}" -f ($stylePath.Substring($repoRoot.Path.Length + 1)))
    exit 2
  }
} else {
  Write-Host ""
  Write-Host "Remaining issues:"
  Write-Host ("- Missing blog CSS: {0}" -f ($stylePath.Substring($repoRoot.Path.Length + 1)))
  exit 2
}

Write-Host ""
Write-Host "Brand sync checks passed."

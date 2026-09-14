@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul
cd /d "%~dp0"
set "LOG=%~dp0_push-log.txt"
echo ==== BAT DAU %DATE% %TIME% ==== > "%LOG%"

REM ============================================================
REM  Push dot noi dung brand page len fastgroup.vn
REM  Repo: https://github.com/minhduckkt/FastGroup.vn  (branch main)
REM  Moi thu duoc ghi vao _push-log.txt de chan doan khi loi.
REM ============================================================

REM ---------- 1. Tim git ----------
set "GIT="
for /f "delims=" %%G in ('where git 2^>nul') do if not defined GIT set "GIT=%%G"
if not defined GIT if exist "%ProgramFiles%\Git\cmd\git.exe" set "GIT=%ProgramFiles%\Git\cmd\git.exe"
if not defined GIT if exist "%ProgramFiles(x86)%\Git\cmd\git.exe" set "GIT=%ProgramFiles(x86)%\Git\cmd\git.exe"
if not defined GIT if exist "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" set "GIT=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"
if not defined GIT if exist "%LOCALAPPDATA%\GitHubDesktop\app-3.5.2\resources\app\git\cmd\git.exe" set "GIT=%LOCALAPPDATA%\GitHubDesktop\app-3.5.2\resources\app\git\cmd\git.exe"

if not defined GIT (
  echo [LOI] Khong tim thay git tren may nay.>> "%LOG%"
  echo.
  echo   [LOI] Khong tim thay git.
  echo   Cai Git for Windows tai https://git-scm.com/download/win
  echo   roi chay lai file nay.
  echo.
  pause
  exit /b 1
)

echo GIT = %GIT% >> "%LOG%"
"%GIT%" --version >> "%LOG%" 2>&1
echo. >> "%LOG%"
echo Thu muc: %CD% >> "%LOG%"
"%GIT%" rev-parse --show-toplevel >> "%LOG%" 2>&1
"%GIT%" remote -v >> "%LOG%" 2>&1
"%GIT%" branch --show-current >> "%LOG%" 2>&1
echo. >> "%LOG%"

echo.
echo Git: %GIT%
echo Repo: %CD%
echo.
echo === Trang thai truoc khi commit ===
"%GIT%" status --short
echo --- status truoc commit --- >> "%LOG%"
"%GIT%" status --short >> "%LOG%" 2>&1
echo.
echo Bam phim bat ky de THEM FILE, hoac dong cua so nay de huy.
pause >nul

REM ---------- 2. Them cac file DA SUA (khong them file moi) ----------
REM  "git add -u" chi dua vao commit nhung file da duoc theo doi va co thay doi.
REM  KHONG dung "git add -A": repo nay PUBLIC, thu muc goc con tai lieu noi bo
REM  (_push-log.txt, HANDOFF-*.md, _tools\qlight, "Claude outputs") khong duoc day len.
"%GIT%" add -u >> "%LOG%" 2>&1
"%GIT%" add ".gitignore" >> "%LOG%" 2>&1
REM  File anh moi (chua duoc git theo doi) phai them tay o day,
REM  vi "git add -u" khong bat file moi.
"%GIT%" add "img/hero-logistics-mobile.webp" >> "%LOG%" 2>&1
"%GIT%" add "wika-viet-nam/assets/brand/wika-logo.webp" >> "%LOG%" 2>&1

echo.
echo === File se duoc commit ===
"%GIT%" status --short
echo --- status sau khi add --- >> "%LOG%"
"%GIT%" status --short >> "%LOG%" 2>&1
echo.
echo Bam phim bat ky de COMMIT va PUSH, hoac dong cua so nay de huy.
pause >nul

REM ---------- 3. Commit ----------
"%GIT%" commit -m "Fix hien thi mobile + gom menu 4 portal thanh mot nut Menu" -m "TRANG CHU fastgroup.vn" -m "- .logo img: them width:auto/max-width:100%%. width=1076 tren the img la presentational hint, gap img{max-width:100%%} nen anh bi ep rong het khung trong khi height van khoa 42px -> chu FAST GROUP ENGINEERING bi keo dai tren moi man hinh <=1150px (do duoc 318x42 thay vi 228x42)" -m "- footer.site img: khoa width:auto cho toan bo anh trong footer" -m "- Hero mobile <=860px: gradient phu doi tu 110deg .93/.82/.55 sang 180deg .88/.74/.82; them text-shadow va nen mo cho nut ghost" -m "- Them img/hero-logistics-mobile.webp (990x1697, cat doc + lam net): ban goc 1920x1061 nam ngang khi cover vao khung doc tren dien thoai bi phong to ~1.9 lan nen mo" -m "- index.html: preload hero tach theo media query, bump ?v=20260915a" -m "PORTAL wika / qlight / endress-hauser / diffu-therm" -m "- Header gon lai con: logo + ten thuong hieu ... [Gui RFQ] [Menu]. Toan bo muc dieu huong nam trong panel so xuong, nhom San pham thut vao" -m "- Lam hoan toan bang CSS trong assets/site.css cua tung portal, KHONG sua ~760 file HTML: tan dung <details class=nav-dropdown> san co lam nut Menu, dung :has() bien <nav class=nav> thanh panel; summary va nut RFQ duoc ghim lai thanh header bang position:absolute nen khong nhay cho khi mo/dong" -m "- Boc trong @supports selector(:has(*)): trinh duyet khong ho tro :has() giu nguyen giao dien cu" -m "- Thanh header cao co dinh (72px / 74px) o moi be rong de hai nut ghim khong lech" -m "- WIKA: thay o vuong chu W bang logo WIKA that (wika-viet-nam/assets/brand/wika-logo.webp, cat sat le tu img/wika-logo.webp)" -m "- Da kiem tra 4 portal x 8 do rong (320-1440px): chieu cao thanh header khong doi, nut khong nhay, ten thuong hieu khong bi cat, khong tran ngang" -m "" -m "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01XW2K95mdmjHurQkbKoRioS" >> "%LOG%" 2>&1
set "RC=%ERRORLEVEL%"
echo commit exit code = %RC% >> "%LOG%"
if not "%RC%"=="0" (
  echo.
  echo   [LOI] commit that bai ^(ma %RC%^). Xem _push-log.txt
  echo.
  type "%LOG%"
  pause
  exit /b 1
)

REM ---------- 4. Push ----------
echo.
echo === Dang push len origin/main ===
"%GIT%" push origin main >> "%LOG%" 2>&1
set "RC=%ERRORLEVEL%"
echo push exit code = %RC% >> "%LOG%"
if not "%RC%"=="0" (
  echo.
  echo   [LOI] push that bai ^(ma %RC%^). Xem _push-log.txt
  echo   Thuong gap: chua dang nhap GitHub tren may nay,
  echo   hoac remote da co commit moi hon ^(chay: git pull --rebase origin main^).
  echo.
  type "%LOG%"
  pause
  exit /b 1
)

"%GIT%" log --oneline -1 >> "%LOG%" 2>&1
echo ==== XONG %DATE% %TIME% ==== >> "%LOG%"

echo.
echo ============================================================
echo   PUSH THANH CONG. GitHub Pages mat 1-3 phut de build lai.
echo   Chi tiet trong _push-log.txt
echo ============================================================
echo.
pause

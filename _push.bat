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

echo.
echo === File se duoc commit ===
"%GIT%" status --short
echo --- status sau khi add --- >> "%LOG%"
"%GIT%" status --short >> "%LOG%" 2>&1
echo.
echo Bam phim bat ky de COMMIT va PUSH, hoac dong cua so nay de huy.
pause >nul

REM ---------- 3. Commit ----------
"%GIT%" commit -m "UI: go thanh lien he noi va muc he thong website, toi uu responsive" -m "- Go .fg-dock (Goi ngay / Zalo / Gui email) khoi 42 trang; them luoi an toan trong CSS" -m "- Tra lai body padding-bottom va vi tri nut len dau trang tren mobile" -m "- Go muc He thong website chuyen nganh khoi index.html va brands.html" -m "- Doi cach dien dat khoi lien ket tren 8 trang brand: bo ngu canh so huu, giu nguyen link" -m "- CSS responsive: breakpoint <=992 / <=600 / <=380px, vung cham >=44px, input 16px chong iOS zoom" -m "- Kiem tra 25 trang x 8 do rong man hinh: khong trang nao tran ngang" -m "" -m "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01WN2jFRP8R2qo9oiS884yFa" >> "%LOG%" 2>&1
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

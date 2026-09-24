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

REM ---------- 0. DANH SACH FILE MOI CUA DOT NAY ----------
REM  QUAN TRONG: "git add -u" chi bat file DA duoc git theo doi.
REM  File MOI TINH (git status hien dau "??") phai liet ke o day,
REM  neu khong commit se bao "nothing added to commit" va push that bai.
REM  Moi dot day noi dung moi thi SUA LAI danh sach nay.
REM  Ghi ca thu muc thi git add se them TOAN BO file ben trong (de quy).
set "NEWFILES=siemens-viet-nam"

set "MSG_TIEUDE=Siemens VN: dang tier B transmitter (439 ma), portal 1107 ma"

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
echo File moi se duoc them tay: %NEWFILES%
echo.
echo Bam phim bat ky de THEM FILE, hoac dong cua so nay de huy.
pause >nul

REM ---------- 2. Them file ----------
REM  "git add -u" dua vao commit nhung file DA duoc theo doi va co thay doi.
REM  KHONG dung "git add -A": repo nay PUBLIC, thu muc goc con tai lieu noi bo
REM  (_push-log.txt, HANDOFF-*.md, _tools\qlight, "Claude outputs") khong duoc day len.
"%GIT%" add -u >> "%LOG%" 2>&1
"%GIT%" add ".gitignore" >> "%LOG%" 2>&1

REM  Them tung file/thu muc moi trong NEWFILES, bao loi ngay neu khong ton tai.
for %%F in (%NEWFILES%) do (
  if exist "%%F" (
    "%GIT%" add "%%F" >> "%LOG%" 2>&1
    echo   + da them %%F
    echo add %%F - OK >> "%LOG%"
  ) else (
    echo   [CANH BAO] khong thay %%F
    echo add %%F - KHONG TIM THAY >> "%LOG%"
  )
)

echo.
echo === File se duoc commit ===
"%GIT%" status --short
echo --- status sau khi add --- >> "%LOG%"
"%GIT%" status --short >> "%LOG%" 2>&1

REM  Neu khong co gi trong staging thi dung lai, bao ro ly do.
"%GIT%" diff --cached --quiet
if "%ERRORLEVEL%"=="0" (
  echo.
  echo   [DUNG] Khong co thay doi nao duoc dua vao commit.
  echo   Neu git status o tren hien dau "??" truoc ten file hoac THU MUC,
  echo   nghia la file do CHUA duoc theo doi. "git add -u" KHONG bat file moi.
  echo   Them duong dan do vao dong "set NEWFILES=" o dau file _push.bat
  echo   roi chay lai. Vi du da gap: anh moi nam ngoai portal -^> img\rosemount
  echo.
  echo Khong co gi trong staging - dung lai. >> "%LOG%"
  pause
  exit /b 1
)

echo.
echo Bam phim bat ky de COMMIT va PUSH, hoac dong cua so nay de huy.
pause >nul

REM ---------- 3. Commit ----------
"%GIT%" commit -m "%MSG_TIEUDE%" -m "TIER B: 439 trang MLFB (DS III 191, P320/P420 92, LH300/LH100 49, TH/TR320 48, P200 21, LU240 15, TF320/420 23)" -m "SEO: tieu de co thuoc tinh phan biet (Ex d/Ex ia/FM-CSA, PA, cap, vat lieu); bang so sanh hien cac thong so khac nhau giua cac ma cung dong; lien ket DS III sang ma P320/P420 de xuat" -m "SUA DU LIEU: dai do P200 so thap phan (0...1,6 bar, 0...0,6 bar abs) truoc bi cat" -m "" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01HTJLJVCv3twkGvchRv9zFM" >> "%LOG%" 2>&1
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
echo   Kiem tra: https://fastgroup.vn/siemens-viet-nam/
echo   Chi tiet trong _push-log.txt
echo ============================================================
echo.
pause

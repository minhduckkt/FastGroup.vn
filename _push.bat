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
set "NEWFILES=brands/kacon.html img/kacon-logo.png img/kacon-og.jpg"

set "MSG_TIEUDE=Them trang thuong hieu KACON + lien ket cheo voi kacon.vn"

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

REM  Them tung file moi trong NEWFILES, bao loi ngay neu file khong ton tai.
for %%F in (%NEWFILES%) do (
  if exist "%%F" (
    "%GIT%" add "%%F" >> "%LOG%" 2>&1
    echo   + da them %%F
    echo add %%F - OK >> "%LOG%"
  ) else (
    echo   [CANH BAO] khong thay file %%F
    echo add %%F - KHONG TIM THAY FILE >> "%LOG%"
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
  echo   Neu git status o tren hien dau "??" truoc ten file,
  echo   nghia la file do CHUA duoc theo doi: them duong dan cua no
  echo   vao dong "set NEWFILES=" o dau file _push.bat roi chay lai.
  echo.
  echo Khong co gi trong staging - dung lai. >> "%LOG%"
  pause
  exit /b 1
)

echo.
echo Bam phim bat ky de COMMIT va PUSH, hoac dong cua so nay de huy.
pause >nul

REM ---------- 3. Commit ----------
"%GIT%" commit -m "%MSG_TIEUDE%" -m "TRANG MOI brands/kacon.html" -m "- Ho so thuong hieu KACON (Korea Auto Controls) theo dung khuon mau trang Honeywell: gioi thieu hang, bang 11 nhom thiet bi kem ky hieu dong, ung dung theo 6 nganh, 4 luu y ky thuat, chung tu theo lo hang, 6 cau FAQ" -m "- SEO: title/description/canonical/hreflang/OG/Twitter + 4 khoi JSON-LD (BreadcrumbList, Brand, WebPage, FAQPage)" -m "- 31 lien ket ra kacon.vn: trang chu, tra cuu part number, tai lieu, shop, lien he, trang dai ly, 11 trang nhom san pham, 7 trang dong san pham" -m "- Cach dat cau: Fast Group la don vi cung ung doc lap, hang KACON chinh hang; chua ghi authorized distributor vi Certificate of Distributor con dang xin" -m "ANH MOI" -m "- img/kacon-logo.png (logo goc, da tach nen ngoai thanh trong suot)" -m "- img/kacon-og.jpg (anh OG dung chung voi kacon.vn)" -m "CAP NHAT brands.html" -m "- Them the KACON vao Nhom 3 (Tu dong hoa and Dieu khien), gan nhan Brand portal" -m "- Cap nhat so thuong hieu 32 -> 33 trong title, description va the OG/Twitter" -m "CAP NHAT sitemap.xml" -m "- Them URL brands/kacon.html, priority 0.64" -m "CAP NHAT _push.bat" -m "- Dua danh sach file moi ra bien NEWFILES o dau file, them vong lap add va canh bao khi file khong ton tai" -m "- Dung lai co thong bao ro rang khi khong co gi trong staging (truoc day commit that bai voi ma 1 ma khong noi ly do)" -m "" -m "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01JMJQwqEU86XzXgUQKB11Q2" >> "%LOG%" 2>&1
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
echo   Kiem tra: https://fastgroup.vn/brands/kacon.html
echo   Chi tiet trong _push-log.txt
echo ============================================================
echo.
pause

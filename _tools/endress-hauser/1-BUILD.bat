@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0..\.."
echo ==========================================================
echo   BUILD portal Endress+Hauser  -  _tools\endress-hauser\build.py
echo ==========================================================
echo.
python "%~dp0build.py"
echo.
echo ==========================================================
echo   Doi chieu:   trang HTML : 221     (moc ngay 13/09/2026)
echo   So trang TANG khi them trang moi - chi can no khong TUT.
echo   Tut xuong tuc la mat trang: dung push, bao Claude.
echo ==========================================================
pause

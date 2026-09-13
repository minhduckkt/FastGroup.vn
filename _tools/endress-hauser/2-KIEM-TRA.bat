@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0..\.."
echo ==========================================================
echo   KIEM TRA portal Endress+Hauser  -  validate2.py
echo ==========================================================
echo.
python "%~dp0validate2.py"
echo.
echo ==========================================================
echo   DAT khi khong con dong LOI nao.
echo   Co dong LOI (...) thi copy toan bo cua so nay gui Claude.
echo ==========================================================
pause

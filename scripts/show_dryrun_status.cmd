@echo off
setlocal
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "D:\test\ft_userdata\show_nfi_risk_duration_600u_dryrun.ps1"
echo.
pause

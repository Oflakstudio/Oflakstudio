@echo off
REM ============================================================
REM   CREA GRAPHIX - Portfolio content sync (Windows)
REM   Double-click this file after you add or change a
REM   certificate, project, or profile photo.
REM ============================================================
cd /d "%~dp0"

where node >nul 2>nul
if errorlevel 1 (
  echo.
  echo   Node.js was not found on this computer.
  echo   Install it from https://nodejs.org  then run this again.
  echo.
  pause
  exit /b 1
)

node sync.js
echo.
echo   Done. You can close this window.
pause

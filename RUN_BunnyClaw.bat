@echo off
title 🐰 BunnyClaw - Private Agent USB

echo.
echo =============================================
echo   🐰 BunnyClaw by Softbite Studio
echo   The Tiny & Mighty Ai Agent USB
echo =============================================
echo.
echo First-time setup: Install Ollama ( ollama.com ) and run:
echo    ollama pull qwen2.5:3b
echo.
echo Starting watcher (auto-replies when you save Ask-Bunny.txt)...
echo.

:: Auto-install watchdog if missing (no admin needed)
python -m pip install watchdog --user >nul 2>&1

start "" "READ_ME_FIRST.html"
start "" "Ask-Bunny.txt"

python watcher.py
pause

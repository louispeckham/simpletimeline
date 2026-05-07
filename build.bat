@echo off
echo ============================================
echo  Timeline - Build Script
echo ============================================
echo.

echo [1/3] Installing dependencies...
pip install pywebview pyinstaller pillow --quiet
if errorlevel 1 (
    echo ERROR: pip install failed. Is Python installed and on PATH?
    pause
    exit /b 1
)

echo [2/3] Building Timeline.exe...
pyinstaller --onefile --noconsole --name Timeline --icon timeline.ico --add-data "timeline.html;." timeline.py
if errorlevel 1 (
    echo ERROR: PyInstaller failed.
    pause
    exit /b 1
)

echo [3/3] Done!
echo.
if exist dist\Timeline.exe (
    echo  SUCCESS!  Your app is at:  dist\Timeline.exe
    echo  You can move Timeline.exe anywhere you like.
    echo  Events are saved in: %%APPDATA%%\Timeline\
) else (
    echo  Build may have failed — check output above.
)
echo.
pause

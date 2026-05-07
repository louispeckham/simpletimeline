TIMELINE — Desktop App
======================

QUICK START
-----------
You need Python 3.8+ installed: https://python.org
(Tick "Add Python to PATH" during install)

  To run without building:   double-click  run.bat
  To build a standalone EXE: double-click  build.bat

After building, your EXE will be at:  dist\Timeline.exe
You can move or copy Timeline.exe anywhere — it runs standalone.

WHERE ARE MY EVENTS SAVED?
--------------------------
Events are stored in:  %APPDATA%\Timeline\
(e.g. C:\Users\YourName\AppData\Roaming\Timeline\)
This means they persist across app restarts and survive updates.

REQUIREMENTS (for build.bat / run.bat only)
-------------------------------------------
- Python 3.8 or newer
- Internet connection on first run (to download pywebview / pyinstaller)
- Windows 10 or 11 (uses Edge WebView2, which is built into Windows)

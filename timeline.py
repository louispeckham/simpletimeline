"""
Timeline — desktop app launcher
Uses pywebview with a Python API bridge for persistent file-based storage,
so events survive across app restarts regardless of WebView localStorage quirks.
"""
import webview
import os
import sys
import shutil
import json

APP_NAME = "Timeline"

def get_app_dir():
    if sys.platform == "win32":
        base = os.environ.get("APPDATA", os.path.expanduser("~"))
    elif sys.platform == "darwin":
        base = os.path.expanduser("~/Library/Application Support")
    else:
        base = os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
    path = os.path.join(base, APP_NAME)
    os.makedirs(path, exist_ok=True)
    return path

def get_source_html():
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS  # type: ignore
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'timeline.html')

class Api:
    """Exposed to JavaScript as window.pywebview.api"""

    def __init__(self, data_file):
        self._data_file = data_file

    def readData(self):
        try:
            with open(self._data_file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return None
        except Exception:
            return None

    def writeData(self, data: str):
        try:
            with open(self._data_file, 'w', encoding='utf-8') as f:
                f.write(data)
            return True
        except Exception:
            return False

def main():
    src = get_source_html()
    if not os.path.exists(src):
        raise FileNotFoundError(f"Could not find timeline.html at {src}")

    app_dir   = get_app_dir()
    dest_html = os.path.join(app_dir, 'timeline.html')
    data_file = os.path.join(app_dir, 'data.json')

    # Update the HTML each run so changes propagate after rebuilds
    shutil.copy2(src, dest_html)

    api = Api(data_file)
    url = 'file:///' + dest_html.replace('\\', '/')

    window = webview.create_window(
        APP_NAME,
        url=url,
        js_api=api,
        width=1280,
        height=800,
        min_size=(800, 500),
    )
    webview.start()

if __name__ == '__main__':
    main()

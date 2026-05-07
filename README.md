# Timeline

A live, scrollable event timeline that runs in your browser or as a standalone Windows desktop app. The current time sits at the top of the screen behind a glowing NOW line, and your events scroll into view as they approach.

---

## Features

- **Live timeline** — moves in real time; the NOW line marks the present moment
- **Add events** with name, date, time, duration, location and colour
- **Drag to reschedule** — move events by dragging, resize by dragging the top or bottom handle, snapping to 5-minute increments
- **Double-click** the timeline to create an event at that time
- **Overlap layout** — simultaneous events split automatically into side-by-side columns
- **Day navigation** — jump forward or back a full calendar day with ◀ ▶
- **Zoom** — 8 zoom levels (toolbar buttons or Ctrl+scroll)
- **Tasks checklist** — a toggleable panel for quick to-dos that disappear when checked
- **Event list** — browse all future or past events in a scrollable panel
- **Persistent storage** — events saved automatically (localStorage in browser, JSON file in the desktop app)
- **Export / Import** — back up and restore all events as a `.json` file

---

## Getting Started

### Browser

Just open `timeline.html` in any modern browser (Chrome, Edge, Firefox). No server or build step needed.

Events are saved to your browser's `localStorage` and persist across page reloads.

### Desktop App (Windows)

**Requirements:** Python 3.8+ from [python.org](https://python.org) — tick **"Add Python to PATH"** during install.

**To run without building:**
```
double-click run.bat
```

**To build a standalone `Timeline.exe`:**
```
double-click build.bat
```

Your executable will be at `dist\Timeline.exe` and can be moved anywhere. Events are saved to `%APPDATA%\Timeline\data.json`.

---

## Usage

### Adding Events

| Method | Description |
|--------|-------------|
| **+ Add Event** button | Opens the event form |
| **Double-click** on the timeline | Opens the form pre-filled to the nearest 15-minute mark |

### Event Form Fields

| Field | Notes |
|-------|-------|
| Name | Event title |
| Date | Type DD/MM/YYYY or use the calendar picker |
| Time | 24-hour format |
| Duration | In minutes |
| Location | Autocompletes from previously used locations |
| Colour | 13 pastel shades |

### Navigating the Timeline

| Action | Result |
|--------|--------|
| **Scroll** | Move forward/backward in time |
| **Ctrl+Scroll** | Zoom in/out |
| **＋ / －** buttons | Zoom in/out |
| **◀ / ▶** buttons | Jump one calendar day |
| **↩ Back to Now** | Return to the live present |

### Editing Events

- **Click** any event card to open the edit form
- **Drag the card body** to move start and end together
- **Drag the top handle** to adjust the start time (end stays fixed)
- **Drag the bottom handle** to adjust the duration

### Tasks

Click **✓ Tasks** to open the checklist panel. Add tasks with the input and press Enter. Click any task to check it off.

### Import / Export

Click **⚙** → **Export Events** to download a `.json` backup. Click **⚙** → **Import Events** to restore.

---

## File Structure

```
timeline.html        # The full single-file web app
timeline.py          # PyWebView launcher for the desktop app
build.bat            # Build Timeline.exe (Windows)
run.bat              # Run without building (Windows)
timeline.ico         # App icon (16 px)
README.md
CHANGELOG.md
```

---

## Browser Compatibility

Tested on Firefox 121+. The desktop app uses Edge WebView2, built into Windows 10 and 11.

---

## License

MIT

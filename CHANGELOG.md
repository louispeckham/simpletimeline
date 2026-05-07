# Changelog

## [1.0.0] — Initial Release

### Core Timeline
- Live-scrolling timeline that moves in real time, with the current moment pinned near the top of the screen behind a glowing **NOW** line
- Time ruler with 15-minute tick marks; hour marks styled distinctly
- Tick labels and the NOW line both use zero-height CSS anchoring so lines align pixel-perfectly with event box edges
- Zoom in / zoom out (8 levels, also via Ctrl+scroll)
- Freeform scroll through time (mouse wheel); **Back to Now** button appears when scrolled away from the present
- Day navigation (◀ ▶) jumps the view to the previous or next calendar day (00:00–24:00), with a date banner displayed at the top of the viewport
- NOW line hidden automatically when the current time is off-screen

### Events
- Add, edit and delete events with name, date, time, duration, location and colour
- 13-colour pastel palette (red → pink rainbow) with subtle tinted card backgrounds
- Custom calendar date picker with month navigation; location field has autocomplete memory (up to 50 previous entries)
- **Double-click** anywhere on the timeline to open a new event pre-filled to the nearest 15-minute tick above the cursor
- New event modal remembers the last-used date, time and duration for quick sequential entry
- Default start time snaps to the next 5-minute increment when opened from the toolbar
- Events **flash** with a yellow glow animation the moment they become active (once per session)
- Ongoing events: text content sticks just below the NOW line as the event scrolls past, sliding back down as the event nears its end
- Past events fade to reduced opacity

### Drag Interaction
- **Move** events by dragging the card body (grab cursor)
- **Resize start** by dragging the top handle (shifts start time, keeps end fixed)
- **Resize end** by dragging the bottom handle (extends or shortens duration)
- All drag operations snap to 5-minute increments; minimum duration 5 minutes

### Overlap Layout
- Events that overlap are automatically arranged into columns using a Union-Find connected-component algorithm with sweep-line maximum-clique detection
- Non-overlapping events always use the full track width

### Tasks Checklist
- Toggleable tasks panel (inline, pushes timeline down)
- Add tasks via text input or Enter key
- Click a task to check it off — animates out and disappears
- Task list is scrollable with a fixed maximum height
- Tasks persisted to localStorage

### Event List
- List Events panel shows all future or past events grouped by date, sorted chronologically
- Toggle between Future (soonest first) and Past (most recent first)
- Click a row to edit; delete button on each row
- Scrollable with date group headings

### Settings Menu
- ⚙ gear menu consolidates Export, Import and Clear All
- Export all events to a `.json` file; import from a `.json` file
- All events stored in `localStorage` (browser) or `%APPDATA%\Timeline\data.json` (desktop app)

### Desktop App (Windows)
- Packaged as a standalone `.exe` via PyWebView + PyInstaller
- Custom scroll icon (`.ico`, 6 sizes: 16–256 px)
- Python file-based storage bridge (`readData` / `writeData` API) so events persist across restarts regardless of WebView localStorage behaviour
- App waits for `pywebviewready` event before loading data; 3-second fallback for browser use
- `build.bat` one-click build script; `run.bat` for running without building

### UI & Design
- Dark theme (`#0a0a0f` background) with yellow accent (`#e8ff6e`) and cyan secondary (`#6ef0ff`)
- Two-row topbar: brand + settings + clock on row 1; actions + zoom + day navigation on row 2
- Monospace clock (DM Mono) prevents layout shift as seconds tick
- All modal overlays: close on backdrop click (mousedown+mouseup on backdrop only — dragging text inside does not dismiss)
- Backdrop blur on modals; calendar popup escapes modal overflow correctly
- `user-select: none` on the viewport prevents text selection on double-click

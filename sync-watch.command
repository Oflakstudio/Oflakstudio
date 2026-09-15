#!/bin/bash
# ============================================================
#   CREA GRAPHIX - Portfolio content sync (WATCH mode, macOS)
#   Double-click to start auto-sync, then LEAVE THIS WINDOW OPEN.
#   Add or rename any certificate, project image or profile photo
#   and content.js updates by itself. Press Ctrl+C to stop.
# ============================================================
cd "$(dirname "$0")"

if ! command -v node >/dev/null 2>&1; then
  echo
  echo "  Node.js was not found. Install it from https://nodejs.org then run again."
  echo
  read -n 1 -s -r -p "Press any key to close..."
  exit 1
fi

echo
echo "  Watching your asset folders... leave this window open."
echo "  Add files and they appear automatically. Press Ctrl+C to stop."
echo
node sync.js --watch

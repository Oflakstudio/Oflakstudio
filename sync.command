#!/bin/bash
# ============================================================
#   CREA GRAPHIX - Portfolio content sync (macOS / Linux)
#   Double-click this file after you add or change a
#   certificate, project, or profile photo.
#   First time on macOS: right-click -> Open (to clear Gatekeeper).
# ============================================================
cd "$(dirname "$0")" || exit 1

if ! command -v node >/dev/null 2>&1; then
  echo
  echo "  Node.js was not found on this computer."
  echo "  Install it from https://nodejs.org  then run this again."
  echo
  read -n 1 -s -r -p "  Press any key to close..."
  echo
  exit 1
fi

node sync.js
echo
read -n 1 -s -r -p "  Done. Press any key to close..."
echo

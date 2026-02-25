#!/usr/bin/env bash
2set -euo pipefail
3
4APP_DIR="$HOME/FlightPriceTracker"
5APP_FILE="flight-app.py"
6PY="python3"
7
8cd "$APP_DIR"
9
10# Pull latest code
11git fetch --all
12git reset --hard origin/main
13
14# Install/update deps
15"$PY" -m pip install -r requirements.txt
16
17# Stop previous process (if any)
18pkill -f "$PY $APP_FILE" || true
19sleep 2
20
21# Start new process
22nohup "$PY" "$APP_FILE" > log.txt 2>&1 &
23echo "Started. Tail logs with: tail -n 200 -f $APP_DIR/log.txt"
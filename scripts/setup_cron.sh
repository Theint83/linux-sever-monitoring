#!/bin/bash

# Member 6: Cron Job Setup Script

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$PROJECT_DIR/run_all.sh"

chmod +x "$SCRIPT_PATH"

# Schedule job every 5 minutes
CRON_JOB="*/5 * * * * /bin/bash $SCRIPT_PATH >> $PROJECT_DIR/cron.log 2>&1"

(crontab -l 2>/dev/null | grep -Fv "$SCRIPT_PATH"; echo "$CRON_JOB") | crontab -

echo "[+] Cron job scheduled successfully."

#!/bin/bash

# ==============================================================================
# Script Name: apache_log_monitor.sh
# Description: A lightweight script to monitor and analyze Apache web server logs.
# ==============================================================================

# Exit immediately if a pipeline returns a non-zero status
set -eo pipefail

# Apache log file paths (Modify these paths if your logs are stored elsewhere)
ACCESS_LOG="/var/log/apache2/access.log"
ERROR_LOG="/var/log/apache2/error.log"

echo "=========================================="
echo "       APACHE WEB SERVER LOG MONITOR      "
echo "=========================================="

# ------------------------------------------------------------------------------
# 1. Analyze Access Log
# ------------------------------------------------------------------------------
echo -e "\n[+] Checking Access Log..."
if [ -f "$ACCESS_LOG" ] && [ -r "$ACCESS_LOG" ]; then
    echo "Total Requests Count:"
    wc -l < "$ACCESS_LOG"
    
    echo -e "\nLast 5 Requests:"
    tail -n 5 "$ACCESS_LOG"
    
    echo -e "\nTop 3 Visitor IPs:"
    # Extracts the first column (IP), counts unique occurrences, and sorts by highest volume
    awk '{print $1}' "$ACCESS_LOG" | sort | uniq -c | sort -nr | head -n 3
else
    echo "[-] Error: Access log file not found or not readable at: $ACCESS_LOG" >&2
fi

# ------------------------------------------------------------------------------
# 2. Analyze Error Log
# ------------------------------------------------------------------------------
echo -e "\n[+] Checking Error Log..."
if [ -f "$ERROR_LOG" ] && [ -r "$ERROR_LOG" ]; then
    echo "Last 5 Error Logs:"
    tail -n 5 "$ERROR_LOG"
else
    echo "[-] Error: Error log file not found or not readable at: $ERROR_LOG" >&2
fi

echo -e "\n=========================================="

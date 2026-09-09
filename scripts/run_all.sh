#!/bin/bash

# Member 6: Automation & Integration Master Script

cd "$(dirname "$0")"

echo "=========================================="
echo "Starting Data Collection Pipeline..."
echo "=========================================="

# Run Database Initialization
python3 init_db.py

# Run Data Collection Scripts
python3 resource_monitor.py 2>/dev/null || true
python3 network_monitor.py 2>/dev/null || true
python3 log_monitor.py 2>/dev/null || true
python3 error_security.py 2>/dev/null || true

echo "=========================================="
echo "All Data Collection Tasks Completed!"
echo "=========================================="

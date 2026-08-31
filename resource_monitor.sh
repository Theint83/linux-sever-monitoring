#!/bin/bash
echo "=== SYSTEM RESOURCE MONITOR ==="
uptime -p
top -bn1 | grep "Cpu(s)" | awk ' {print "CPU Load: " 100- $8 "%"}'
free -h
df -h /

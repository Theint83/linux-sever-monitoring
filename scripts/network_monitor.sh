#!/bin/bash
ip_addr=$(ip -4 addr show enp0s3 | ask '/inet / {print $2}' | cut -d/ -f1)
net_interface="enp0s3"
if ping -c 1 -W 2 8.8.8.8 > /dev/null 2>&1; then 
net_status="Connected"
else
net_status="Disconnected"
fi
rx_bytes=$(cat /sys/class/net/enp0s3/statistics/rx_bytes)
tx_bytes=$(cat /sys/class/net/enp0s3/statistics/tx_bytes)
rx_mb=$(awk "BEGIN {printf \"%.2f\", $rx_bytes/1024/1024}")
tx_mb=$(awk "BEGIN {printf \"%.2f\", $tx_bytes/1024/1024}")
echo "---Network Monitoring ---"
echo "IP Address: $ip_addr | Status: $net_status | Interface: $net_interface | RX: $rx_mb MB | TX: $tx_mb MB"





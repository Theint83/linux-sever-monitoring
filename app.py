from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = "monitoring.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/monitoring-data', methods=['GET'])
def get_monitoring_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM system_resources ORDER BY id DESC LIMIT 1")
        res_row = cursor.fetchone()
        system_resources = dict(res_row) if res_row else {
            "uptime": "N/A", "cpu_usage": 0, "ram_usage": "0", "disk_usage": "0"
        }

        cursor.execute("SELECT * FROM network_stats ORDER BY id DESC LIMIT 1")
        net_row = cursor.fetchone()
        network_stats = dict(net_row) if net_row else {
            "ip_address": "127.0.0.1", "net_status": "RUNNING"
        }

        cursor.execute("SELECT COUNT(*) as alert_count FROM security_alerts")
        alert_row = cursor.fetchone()
        security_alerts = alert_row["alert_count"] if alert_row else 0

        cursor.execute("SELECT * FROM server_logs ORDER BY id DESC LIMIT 5")
        logs_rows = cursor.fetchall()
        server_logs = [dict(row) for row in logs_rows]

        conn.close()

        return jsonify({
            "system_resources": system_resources,
            "network_stats": network_stats,
            "security_alerts": security_alerts,
            "server_logs": server_logs
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

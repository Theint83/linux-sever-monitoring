import sqlite3

def init_db():
    conn = sqlite3.connect("monitoring.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        uptime TEXT,
        cpu_usage REAL,
        ram_usage TEXT,
        disk_usage TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS network_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        ip_address TEXT,
        interface TEXT,
        net_status TEXT,
        rx_mb REAL,
        tx_mb REAL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS server_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        log_type TEXT,
        client_ip TEXT,
        request_method TEXT,
        status_code INTEGER,
        log_message TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        source_ip TEXT,
        alert_type TEXT,
        severity TEXT,
        description TEXT
    );
    """)

    conn.commit()
    conn.close()
    print("[+] Database initialized successfully.")

if __name__ == "__main__":
    init_db()

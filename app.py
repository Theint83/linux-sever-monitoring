from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import socket 
import time 
from datetime import datetime

app=Flask(__name__)
CORS(app)

boot_time = psutil.boot_time()
logs_list=[]
log_id_counter=1	
@app.route('/api/monitoring-data')
def get_monitoring_data():
	global log_id_counter,logs_list
	uptime_seconds = int(time.time() - boot_time)
	days,remainder=divmod(uptime_seconds,86400)
	hours,remainder=divmod(uptime_seconds,3600)
	minutes,seconds=divmod(remainder,60)
	uptime_str = f"{days}d {hours}h {minutes}m"
	
	
	disk=psutil.disk_usage('/')
	cpu=psutil.cpu_percent(interval=0.5)
	ram=psutil.virtual_memory().percent
	
	alerts=0
	if cpu>70: alerts +=1
	if ram>80:alerts += 1
	
	now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	new_logs={	
		"id":log_id_counter,
		"timestamp":now_str,
		"message": f"System Check: CPU ({cpu}%),RAM ({ram}%)",
		"Level": "Warning" if (cpu > 70 or ram >80) else "INFO"
	}
	logs_list=[]
	log_id_counter = 1

	if len(logs_list) > 10:
        	logs_list = logs_list[:10]

	return jsonify({
	"server_status": "Running",
	"ip_address": socket.gethostbyname(socket.gethostname()),
	"uptime": uptime_str,
	"security_warnings": alerts,
	"cpu_usage": cpu,
	"ram_usage": ram,
	"disk_used": round(disk.used /(1024**3),2),
	"disk_free": round(disk.free / (1024**3),2),
	"logs": logs_list,
	"network_stats":{
		"net_status": "ONLINE"}
	})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)




import speedtest
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(host="localhost", user="root", password="password", database="data")

servers = []
threads = None
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()
res = s.results.dict()

cursor = db.cursor()

sql = "INSERT INTO speedtest (download, upload, ping, dt) VALUES (%s, %s, %s, %s)"
val = (int(res["download"]), int(res["upload"]), float(res["ping"]), datetime.strptime(res["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ"))

cursor.execute(sql, val)
db.commit()

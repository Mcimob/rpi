import speedtest
import mysql.connector
from datetime import datetime
import time

time.sleep(15)

db = mysql.connector.connect(host="db", user="root", password="password", database="data")
cursor = db.cursor()

servers = []
threads = None
try:
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()
    res = s.results.dict()

    sql = "INSERT INTO speedtest (download, upload, ping, dt) VALUES (%s, %s, %s, %s)"
    val = (int(res["download"]), int(res["upload"]), float(res["ping"]), datetime.strptime(res["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ"))
    cursor.execute(sql, val)

    

except speedtest.ConfigRetrievalError:
    print("Connection error")

    sql = "INSERT INTO speedtest_errors (dt, Errortype) VALUES (%s, %s)"
    val = (datetime.now(), "Connection Error")
    cursor.execute(sql, val)



db.commit()

#!/usr/bin/env python3

from tabulate import tabulate
import mysql.connector
import config
import json

db = mysql.connector.connect(
  host=config.host,
  user=config.user,
  password=config.password,
  database="quest"
)
cur = db.cursor(dictionary=True)

sql = "SELECT * FROM quest q1 WHERE timestamp = (SELECT MAX(timestamp) FROM quest q2 WHERE q1.serial = q2.serial) ORDER BY timestamp DESC"
cur.execute(sql)
results = cur.fetchall()

filtered_results = []

for r in results:
    j = json.loads(r["json"])
    battery = f'{j["battery"]["level"]}%{" and charging" if j["battery"]["charging"] else ", not charging"}'
    appStatus = "OK"
    for desired_app in config.apps:
      found = False
      for installed_app in j["appsList"]:
        if desired_app["packageName"] == installed_app["packageName"]:
          found = True
          if desired_app["versionName"] != installed_app["versionName"]:
            appStatus = f'{desired_app["packageName"]} wants {desired_app["versionName"]} but {installed_app["versionName"]} is installed'
      if not found:
        appStatus = f'{desired_app["packageName"]} not installed'
    filtered_results.append([r["serial"], r["timestamp"], r["ip"], battery, j["sysInfo"]["buildDisplay"], len(j["appsList"]), appStatus])

print(tabulate(filtered_results, headers=["Serial", "Last updated", "Last IP", "Last Battery State", "OS version", "Installed apps count", "App status"]))
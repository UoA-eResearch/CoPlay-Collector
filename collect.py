#!/usr/bin/env python3

from netaddr import IPNetwork
import sys
import requests
from requests.exceptions import RequestException
from tqdm.auto import tqdm
import mysql.connector
import json
import config

try:
    network = list(IPNetwork(config.subnet))
    print(f"Scanning {network[0]} to {network[-1]}")
except:
    network = config.ips

db = mysql.connector.connect(
  host=config.host,
  user=config.user,
  password=config.password,
  database=config.database
)
cur = db.cursor()

for ip in tqdm(network):
    try:
        r = requests.get(f"http://{ip}:8080/get-json", timeout=(3.05, 27)) # connect, read
        r.raise_for_status()
    except RequestException:
        continue
    data = r.json()
    serial = data["sysInfo"]["serial"]
    print(ip, serial)
    sql = "INSERT IGNORE INTO quest (ip, serial, json) VALUES (%s, %s, %s)"
    val = (str(ip), serial, json.dumps(data))
    cur.execute(sql, val)
    db.commit()
#//+------------------------------------------------------------------+
#//|                                VerysVeryInc.POSforFreee.MySQL.py |
#//|                  Copyright(c) 2018, VerysVery Inc. & Yoshio.Mr24 |
#//|                      https://github.com/MatsuoStation/Freee.POS/ |
#//|                                                 Since:2018.02.27 |
#//|                                Released under the Apache license |
#//|                       https://opensource.org/licenses/Apache-2.0 |
#//|         "VsV.POSforFreee.MySQL.py - Ver.0.0.2 Update:2018.02.27" |
#//+------------------------------------------------------------------+
#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Python3 : Setup ###
import json
from urllib.parse import urlparse

### MySQL : Setup ###
import mysql.connector


### JSON : Setup ###
try:
	with open ('awsconfig.json', 'r') as f:
		data = json.load(f)
		# print(data)
except json.JSONDecodeError as e:
	print('JSONDecodeError: ' , e)


### MySQL : Connector ###
config = data

cnn = mysql.connector.connect(**config)
cur = cnn.cursor(buffered=True)
cur.execute("SHOW STATUS LIKE 'Uptime'")
print(cur.fetchone())

cur.close()

cnn.close()

#+------------------------------------------------------------------+
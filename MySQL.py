#//+------------------------------------------------------------------+
#//|                                VerysVeryInc.POSforFreee.MySQL.py |
#//|                  Copyright(c) 2018, VerysVery Inc. & Yoshio.Mr24 |
#//|                      https://github.com/MatsuoStation/Freee.POS/ |
#//|                                                 Since:2018.02.27 |
#//|                                Released under the Apache license |
#//|                       https://opensource.org/licenses/Apache-2.0 |
#//|         "VsV.POSforFreee.MySQL.py - Ver.0.0.1 Update:2018.02.27" |
#//+------------------------------------------------------------------+
#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Python3 : Setup ###
from urllib.parse import urlparse

### MySQL : Setup ###
import mysql.connector


### AWS.RDS : Setup ###
config = {
	'user': '<YOUR AWS RDS USER NAME>',
	'password': '<YOUR AWS RDS PASSWORD>',
	'host': '<YOUR AWS RDS HOST URL>',
	'database': '<YOUR AWS RDS DATABASE NAME>',
}

cnn = mysql.connector.connect(**config)
cur = cnn.cursor(buffered=True)
cur.execute("SHOW STATUS LIKE 'Uptime'")
print(cur.fetchone())

cur.close()

cnn.close()

#+------------------------------------------------------------------+
#!/usr/bin/python
import urllib2
import MySQLdb
import sys
import time

mysql_connection = MySQLdb.connect(host="192.168.1.17", user="monitoring", passwd="AzMb3_1$", db="monitoring")
cursor = mysql_connection.cursor()
try:
	cursor.execute("""SELECT id_site, site FROM sites WHERE enabled=1""")
	data = cursor.fetchall()
except:
	print "SQL Error"

for row in data:
	id_site = row[0]
	site = row[1]
	try:
		code = urllib2.urlopen(site).code
	except urllib2.HTTPError as e:
		code = e.code
	try:
		id_site = id_site
		code = code
		cursor.execute("""INSERT INTO monlog (fk_site, state) VALUES (%s, %s)""", (id_site, code))
		mysql_connection.commit()
	except:
		print "SQL Error"

cursor.close()
mysql_connection.close()

#!/usr/bin/python
import MySQLdb
import sys

mysql_connection = MySQLdb.connect(host="192.168.1.17", user="monitoring", passwd="AzMb3_1$", db="monitoring")
cursor = mysql_connection.cursor()

#cursor.execute("""INSERT INTO monlog (fk_site, state) VALUES ('1', '100')""")
#mysql_connection.commit()

cursor.execute("""SELECT id_site, site FROM sites WHERE enabled=1""")
data = cursor.fetchall()

for row in data:
	print row[0], row[1]


mysql_connection.close()

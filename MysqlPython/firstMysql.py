# encoding:utf-8

import MySQLdb

db = MySQLdb.connect('10.1.1.159','shuanglong','shuanglong','test')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
cursor.execute("select * from t_test")
res = cursor.fetchall()
for record in res:
	print record
print 'Database Version: %s' % data
db.close()

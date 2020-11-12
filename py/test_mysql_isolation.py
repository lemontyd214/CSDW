import MySQLdb

if __name__ == "__main__":
	conn = MySQLdb.connect("localhost", "root", "", "csdw", charset="utf8")
	cursor = conn.cursor()

	try:
		sql = "set session transaction isolation level read uncommitted;"
		cursor.execute(sql)
		sql1 = "update player_name set name='test' where id=919989;"
		cursor.execute(sql1)
		sql2 = "select id, name from player_name where id=919989;"
		cursor.execute(sql2)
		result = cursor.fetchone()
		print(result)
		conn.commit()
		cursor.close()
		conn.close()
	except MySQLdb.Error, e:
		conn.rollback()
		print("error {} {}".format(e.args[0], e.args[1]))
	# try:
	# 	sql1 = "SELECT @@global.tx_isolation;"
	# 	cursor.execute(sql1)
	# 	result1 = cursor.fetchone()
	# 	print("previous global isolation: {}".format(result1))
	# 	sql2 = "SELECT @@session.tx_isolation;"
	# 	cursor.execute(sql2)
	# 	result2 = cursor.fetchone()
	# 	print("previous session isolation: {}".format(result2))
	# 	sql3 = "set session transaction isolation level read uncommitted;"
	# 	cursor.execute(sql3)
	# 	result3 = cursor.fetchone()
	# 	print("change session isolation result: {}".format(result3))
	# except:
	# 	print("error")
	# finally:
	# 	sql4 = "SELECT @@session.tx_isolation;"
	# 	cursor.execute(sql4)
	# 	result4 = cursor.fetchone()
	# 	print("current session isolation: {}".format(result4))

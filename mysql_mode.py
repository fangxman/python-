#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#filename:mysql_mode.py
#author:man

# import MySQLdb
import pymysql
import sys
sys.path.append("/var/www/html/cloudmap_taihang/jiaoben/py_pack")
import tools_mode

db_conf_path = "/var/www/html/cloudmap_taihang/configFile/mysql.cfg"


def __help__():
	print ("函数说明".center(120,"-"))
	print ()
	print ("__help__			=>		帮助")
	print ("db_conn				=>		连接数据库")
	print ("exec_sql_num			=>		执行sql语句,返回值是操作的数量")
	print ("exec_sql_num_dict		=>		执行sql语句,返回值是操作的数量")
	print ("exec_sql_id			=>		执行sql语句,返回值是插入成功的id")
	print ("exec_sql_id_dict		=>		执行sql语句,返回值是插入成功的id")
	print ("exec_select_num			=>		执行sql语句,返回值是查询的结果的数量")
	print ("exec_select_num_dict		=>		执行sql语句,返回值是查询的结果的数量")
	print ("exec_select_one			=>		执行sql语句,返回值是查询的结果的第一条数据")
	print ("exec_select_one_dict		=>		执行sql语句,返回值是查询的结果的第一条数据")
	print ("exec_select_all			=>		执行sql语句,返回值是查询的结果")
	print ("exec_select_all_dict		=>		执行sql语句,返回值是查询的结果")
	print ("exec_select_row			=>		不需要先连接数据库,执行sql语句,直接返回第一行的结果")
	print ("exec_select_result		=>		不需要先连接数据库,执行sql语句,直接返回所有的结果")
	print ("exec_select_rowCol		=>		不需要先连接数据库,执行sql语句,直接返回第一行的第一列的值")
	print ("exec_sql_num_noConn		=>		不需要先连接数据库,执行sql语句,适合使用 update insert ")
	print ()
	print ("说明结束".center(120,"-"))
	
	
"""
连接数据库
返回值是数据库连接
"""
def db_conn():
	config_dict = tools_mode.get_config(db_conf_path)
	db = pymysql.connect(host = str(config_dict['host']), user = str(config_dict['user']), password = str(config_dict['password']), database = str(config_dict['database']))
	return db
	
"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句
返回值是操作的数量
"""
def exec_sql_num(db, cursor, sql):
	num = 0
	try:
		# 执行sql语句
		num = cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
	except:
		# 发生错误时回滚
		db.rollback()
	return num
	

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是操作的数量
列子 ：
	1、mysql_mode.exec_sql_num_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%(IP)s  " , {"IP":"192.168.2.32"})
	2、mysql_mode.exec_sql_num_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%s AND MAC=%s  " , ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_sql_num_dict(db, cursor, sql, dict):
	num = 0
	try:
		#执行sql语句
		num = cursor.execute(sql, dict)
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return num

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句
返回值是插入成功的id
"""
def exec_sql_id(db, cursor, sql):
	id = 0
	try:
		# 执行sql语句
		cursor.execute(sql)
		#获取插入的id值
		id = cursor.lastrowid
		# 提交到数据库执行
		db.commit()
	except:
		# 发生错误时回滚
		db.rollback()
	return id
	
"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是插入成功的id
列子:
	1、mysql_mode.exec_sql_id_dict(db,cursor,"INSERT INTO log_control(IP) VALUES(%(IP)s)  " , {"IP":"192.168.2.32"})
	2、mysql_mode.exec_sql_id_dict(db,cursor,"INSERT INTO log_control(IP) VALUES(%s,%s)  " , ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_sql_id_dict(db, cursor, sql, dict):
	id = 0
	try:
		#执行sql语句
		num = cursor.execute(sql, dict)
		#获取插入的id值
		id = cursor.lastrowid
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return id

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句
返回值是查询的结果的数量
"""
def exec_select_num(db, cursor, sql):
	num = 0
	try:
		#执行sql语句
		cursor.execute(sql)
		#获取查询的条数
		num = cursor.rowcount
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return num

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是查询的结果的数量
列子:
	1、mysql_mode.exec_select_num_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%(IP)s  " , {"IP":"192.168.2.32"})
	2、mysql_mode.exec_select_num_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%s AND MAC=%s " , ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_select_num_dict(db, cursor, sql, dict):
	num = 0
	try:
		#执行sql语句
		cursor.execute(sql, dict)
		#获取查询的条数
		num = cursor.rowcount
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return num

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句
返回值是查询的结果的第一条数据
"""
def exec_select_one(db, cursor, sql):
	result = ()
	try:
		#执行sql语句
		cursor.execute(sql)
		#获取查询的条数
		result = cursor.fetchone()
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return result

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是查询的结果的第一条数据
列子：
	1、mysql_mode.exec_select_one_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%(IP)s  " , {"IP":"192.168.2.32"})
	2、mysql_mode.exec_sql_num_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%s AND MAC=%s  " , ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_select_one_dict(db, cursor, sql, dict):
	result = ()
	try:
		#执行sql语句
		cursor.execute(sql, dict)
		#获取查询的条数
		result = cursor.fetchone()
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return result

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句
返回值是查询的结果
"""
def exec_select_all(db, cursor, sql):
	result = ()
	try:
		#执行sql语句
		cursor.execute(sql)
		#获取查询的条数
		result = cursor.fetchall()
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return result

"""
执行sql语句
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是查询的结果
列子：
	1、mysql_mode.exec_select_all_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%(IP)s  " , {"IP":"192.168.2.32"})
	2、mysql_mode.exec_select_all_dict(db,cursor,"SELECT * FROM log_control WHERE IP=%s AND MAC=%s  " , ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_select_all_dict(db, cursor, sql, dict):
	result = ()
	try:
		#执行sql语句
		cursor.execute(sql, dict)
		#获取查询的条数
		result = cursor.fetchall()
		# 提交到数据库执行
		db.commit()
	except:
		#发生错误时回滚
		db.rollback()
	return result

"""
不需要先连接数据库,执行sql语句,直接返回查询的结果的数量
参数说明
sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是查询的结果的数量
列子：
	1、mysql_mode.exec_select_rowcount("SELECT * FROM log_control")
	2、mysql_mode.exec_select_rowcount("SELECT * FROM log_control")
	2、mysql_mode.exec_select_rowcount("SELECT * FROM log_control WHERE IP=%(IP)s", {"IP":"192.168.2.32"})
	2、mysql_mode.exec_select_rowcount("SELECT * FROM log_control WHERE IP=%s AND MAC=%s", ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_select_rowcount(sql, dict = []):
	db = db_conn()
	num = 0
	if dict != []:
		num = exec_select_num_dict(db, db.cursor(), sql, dict)
	else:
		num = exec_select_num(db, db.cursor(), sql)
	db.close()
	return num

"""
不需要先连接数据库,执行sql语句,直接返回第一行的结果
参数说明
sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是查询的结果
列子：
	1、mysql_mode.exec_select_row("SELECT * FROM log_control")
	2、mysql_mode.exec_select_row("SELECT * FROM log_control")
	2、mysql_mode.exec_select_row("SELECT * FROM log_control WHERE IP=%(IP)s", {"IP":"192.168.2.32"})
	2、mysql_mode.exec_select_row("SELECT * FROM log_control WHERE IP=%s AND MAC=%s", ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_select_row(sql, dict = []):
	db = db_conn()
	result = ()
	if dict != []:
		result = exec_select_one_dict(db, db.cursor(), sql, dict)
	else:
		result = exec_select_one(db, db.cursor(), sql)
	db.close()
	return result

"""
不需要先连接数据库,执行sql语句,直接返回所有的结果
参数说明
sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是查询的结果
列子：
	1、mysql_mode.exec_select_result("SELECT * FROM log_control")
	2、mysql_mode.exec_select_result("SELECT * FROM log_control")
	2、mysql_mode.exec_select_result("SELECT * FROM log_control WHERE IP=%(IP)s", {"IP":"192.168.2.32"})
	2、mysql_mode.exec_select_result("SELECT * FROM log_control WHERE IP=%s AND MAC=%s", ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_select_result(sql, dict = []):
	db = db_conn()
	result = ()
	if dict != []:
		result = exec_select_all_dict(db, db.cursor(), sql, dict)
	else:
		result = exec_select_all(db, db.cursor(), sql)
	db.close()
	return result

"""
不需要先连接数据库,执行sql语句,直接返回第一行的第一列的值
参数说明
sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是查询的结果第一列的值,没有则返回0
列子：
	1、mysql_mode.exec_select_rowCol("SELECT id FROM log_control")
	2、mysql_mode.exec_select_rowCol("SELECT id FROM log_control")
	2、mysql_mode.exec_select_rowCol("SELECT id FROM log_control WHERE IP=%(IP)s", {"IP":"192.168.2.32"})
	2、mysql_mode.exec_select_rowCol("SELECT id FROM log_control WHERE IP=%s AND MAC=%s", ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_select_rowCol(sql, dict = []):
	db = db_conn()
	result = ()
	if dict != []:
		result = exec_select_one_dict(db, db.cursor(), sql, dict)
	else:
		result = exec_select_one(db, db.cursor(), sql)
	
	db.close()
	if result:
		return result[0]
	else:
		return 0

"""
不需要先连接数据库,执行sql语句,适合使用 update insert 
参数说明
db:数据库连接,cursor:数据库的操作游标,sql:待执行的sql语句,dict:是数据绑定的数据(是字典的格式或者是列表的格式)
返回值是操作的数量
列子 ：
	1、mysql_mode.exec_sql_num_noConn("SELECT * FROM log_control WHERE IP=%(IP)s  " , {"IP":"192.168.2.32"})
	2、mysql_mode.exec_sql_num_noConn("SELECT * FROM log_control WHERE IP=%s AND MAC=%s  " , ["192.168.2.32","00:11:22:33:44:55"])
"""
def exec_sql_num_noConn(sql, dict = []):
	num = 0
	db = db_conn()
	if dict != []:
		num = exec_sql_num_dict(db, db.cursor(), sql, dict)
	else:
		num = exec_sql_num(db, db.cursor(), sql)
	
	db.close()
	return num


if __name__ == "__main__":
	__help__()
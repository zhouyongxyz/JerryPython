#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "12345678")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

cursor.execute('show databases')
rows = cursor.fetchall()
for row in rows:
    tmp = "%2s" % row
    print("row = " + str(row))

print("tmp = %s"%tmp)

dbname = "test2"
cursor.execute('create database if not exists ' + dbname)

# 提交到数据库执行
db.commit()

# 关闭数据库连接
db.close()
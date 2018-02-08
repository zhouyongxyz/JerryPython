#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz
# mysqldb.py
import pymysql
import time

mysql_user = "root"
mysql_pwd = "12345678"
mysql_db = "taskserver"

class MySQLUtil():
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.pwd = "12345678"
        self.dbName = "taskserver"
        pass


    def saveMessage(self,ipAddr,msg,isServer):
        # try to connect mysql server
        self.db = pymysql.connect(self.host, self.user, self.pwd, self.dbName)
        self.cursor = self.db.cursor()
        now = time.strftime("%m/%d %H:%M:%S", time.localtime())
        sql = "INSERT INTO messages(ipaddr, \
               message, isserver, date) \
               VALUES ('%s', '%s', '%d', '%s')" % \
              (ipAddr, msg, 1 if isServer == True else 0, now)
        try:
            # excute the sql
            self.cursor.execute(sql)
            # commit the operation
            self.db.commit()
        except:
            # rollback the operation
            self.db.rollback()

        # close mysql connect
        self.db.close()
        pass

    def getMessages(self,ipAddr):
        messages = []
        self.db = pymysql.connect(self.host, self.user, self.pwd, self.dbName)
        self.cursor = self.db.cursor()
        now = time.strftime("%m/%d %H:%M:%S", time.localtime())
        sql = "select * from messages where ipaddr = '%s' " % ipAddr
        try:
            # excute the sql
            self.cursor.execute(sql)
            # commit the operation
            results = self.cursor.fetchall()
            msg = {}
            for row in results:
                msg['ipaddr'] = row[0]
                msg['msg'] = row[1]
                msg['isserver'] = row[2]
                msg['date'] = row[3]
                messages.append(msg)

            return messages

        except:
            # rollback the operation
            self.db.rollback()

        # close mysql connect
        self.db.close()
        pass

    # just for test
    def test(self):
        timeStr = time.strftime("%m/%d %H:%M:%S",time.localtime())
        print(timeStr)

# test mysqlUtil
if __name__ == "__main__":
    mysql = MySQLUtil()
    mysql.test()
    #mysql.saveMessage("127.0.0.1","hello world2",True)
    msgs = mysql.getMessages("127.0.0.1")
    print("msgs = {}".format(msgs))
    for msg in msgs:
        print("msg = {}".format(msg))
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz
# sqlite3db.py
import sqlite3
import time

class Sqlite3Util():
    def __init__(self,dbName = "taskserver.db"):
        self.dbName = dbName
        self.conn = sqlite3.connect(self.dbName)
        print("create table if not exist ...")

        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages
               (id              INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
               ipaddr           TEXT    NOT NULL,
               message          TEXT     NOT NULL,
               isserver         INT     NOT NULL,
               date             TEXT    NOT NULL);''')
        print("Table created successfully")
        self.conn.commit()
        self.conn.close()
        pass


    def saveMessage(self,ipAddr,msg,isServer):
        # try to connect mysql server
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()
        now = time.strftime("%m/%d %H:%M:%S", time.localtime())
        sql = "INSERT INTO messages(ipaddr, \
               message, isserver, date) \
               VALUES ('%s', '%s', '%d', '%s')" % \
              (ipAddr, msg, 1 if isServer == True else 0, now)
        try:
            # excute the sql
            self.cursor.execute(sql)
            # commit the operation
            self.conn.commit()
        except:
            # rollback the operation
            self.conn.rollback()

        # close mysql connect
        self.conn.close()
        pass

    def getMessages(self,ipAddr):
        messages = []
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()
        now = time.strftime("%m/%d %H:%M:%S", time.localtime())
        sql = "select * from messages where ipaddr = '%s' " % ipAddr
        try:
            # excute the sql
            self.cursor.execute(sql)
            # commit the operation
            results = self.cursor.fetchall()
            for row in results:
                msg = {}
                msg['ipaddr'] = row[1]
                msg['msg'] = row[2]
                msg['isserver'] = row[3]
                msg['date'] = row[4]
                messages.append(msg)

            return messages

        except:
            # rollback the operation
            self.conn.rollback()

        # close mysql connect
        self.conn.close()
        pass

    # just for test
    def test(self):
        timeStr = time.strftime("%m/%d %H:%M:%S",time.localtime())
        print(timeStr)

# test mysqlUtil
if __name__ == "__main__":
    sq = Sqlite3Util()
    sq.test()
    #sq.saveMessage("127.0.0.1","hello world",True)
    msgs = sq.getMessages("127.0.0.1")
    print("msgs = {}".format(msgs))
    for msg in msgs:
        print("msg = {}".format(msg))
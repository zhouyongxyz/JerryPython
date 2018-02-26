#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz
# server.py

from PyQt5.QtWidgets import QApplication, QWidget ,QMainWindow,QInputDialog,QFileDialog,QMessageBox,QTreeWidgetItem   #导入相应的包
from PyQt5.QtNetwork import (QHostAddress, QTcpServer, QTcpSocket)
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
import sys
import re
import socketserver
import _thread
import json
from serverui import Ui_MainWindow
from TcpServer import TcpServer
from mysqldb import MySQLUtil
from sqlite3db import Sqlite3Util
from LuaEditor import PythonHighlighter

PORT = 9008
class TaskServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        # clientTreeWidget [QTreeWidget]
        # contentTabWiget [QTabWidget]
        # content_ipaddr  [QLabel]
        # content_status [QTextEdit]
        # edit_cmd [QLineEdit]
        self.ui.setupUi(self)
        self.ui.btn_send.clicked.connect(self.btnSendRemoteCmd)
        self.ui.btn_file.clicked.connect(self.btnAddScriptFile)
        self.ui.clientTreeWidget.itemClicked.connect(self.treeItemClicked)
        self.ui.btn_run.clicked.connect(self.btnRunLua)

        font = QFont("New Courier", 11)
        self.ui.code_editor.setFont(font)
        #high light the lua code
        self.highlighter = PythonHighlighter(self.ui.code_editor.document())


        self.clientHandlerList = []
        self.clientNameList = []
        self.initUI()

        self.tcpServer = TcpServer(self)
        if not self.tcpServer.listen(QHostAddress("0.0.0.0"), PORT):
            QMessageBox.critical(self, "Building Services Server",
                                 "Failed to start server: {0}".format(self.tcpServer.errorString()))
            self.close()
            return
        # init the db
        # self.db = MySQLUtil()
        self.db = Sqlite3Util()

    def initUI(self):
        #init tree view
        self.treeRoot = QTreeWidgetItem(self.ui.clientTreeWidget);
        self.treeRoot.setText(0, '网络1')
        self.ui.clientTreeWidget.addTopLevelItem(self.treeRoot)
        pass
    # send cmd to client
    def btnSendRemoteCmd(self):
        # text, ok = QInputDialog.getText(self, 'Input Dialog',
        #                                 'Enter your name:')
        # if ok:
        #     print("hello")
        cmd = self.ui.edit_cmd.text()
        self.tcpServer.sendMessage(self.ui.content_ipaddr.text(),cmd)
        self.db.saveMessage(self.ui.content_ipaddr.text(),cmd,True)
        self.showMessage(self.ui.content_ipaddr.text())
        print("cmd = " + cmd)

    def btnAddScriptFile(self):
        print("btnAddScriptFile")
        fname = QFileDialog.getOpenFileName(self, 'Open Script File', '/home')
        print("select fname[0] = " + fname[0])

    def treeItemClicked(self,item,column):
        print("treeItemClicked" + item.text(column))
        content = item.text(column)
        if re.match( r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content):
            print("ip : " + content)
            self.ui.content_ipaddr.setText(content)
            self.showMessage(content)




    def addSocketClient(self,client):
        print("addSocketClient ...")

    def clientConnect(self,ipAddr):
        print("client connect ipAddr = " + ipAddr)
        _translate = QtCore.QCoreApplication.translate
        print("topLevel size = " + str(self.ui.clientTreeWidget.topLevelItem(0).childCount()))
        index = self.ui.clientTreeWidget.topLevelItem(0).childCount()
        #self.ui.clientTreeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", ipAddr))
        item = QTreeWidgetItem(self.treeRoot);
        item.setText(index,ipAddr)

    def recvMessage(self, ipAddr, msg):
        currentClient = self.ui.content_ipaddr.text()
        self.db.saveMessage(ipAddr,msg,False)
        if currentClient == ipAddr:
            self.showMessage(ipAddr)
        pass

    def showMessage(self,ipAddr):
        print("showMessage:{}".format(ipAddr))
        messages = self.db.getMessages(ipAddr)
        statusStr = "";
        if messages:
            for msg in messages:
                if msg['isserver'] == 1:
                    statusStr += "server[%s] -> :" % msg['date']
                else:
                    statusStr += "client[%s] -> :" % msg['date']
                statusStr += msg['msg'] + " \n"

        self.ui.content_status.setText(statusStr)

    # send lua script to client
    def btnRunLua(self):
        lua = self.ui.code_editor.toPlainText()
        #print("lua :" + lua)
        data = {}
        data["action"] = "script"
        data["lua"] = lua
        print(json.dumps(data))
        data = json.dumps(data)
        print("len = {}" .format(len(data)))
        head = "data-{:05d}".format(len(data))
        self.tcpServer.sendLuaMessage(self.ui.content_ipaddr.text(), head + data)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TaskServerWindow()
    w.show()
    sys.exit(app.exec_())
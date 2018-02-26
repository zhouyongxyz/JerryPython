#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz
# TcpServer.py
from PyQt5.QtNetwork import (QHostAddress, QTcpServer, QTcpSocket)
from PyQt5.QtCore import (QByteArray, QDataStream, QDate, QIODevice, Qt)

SIZEOF_UINT16 = 2

class TcpSocket(QTcpSocket):

    def __init__(self, parent=None):
        super(TcpSocket, self).__init__(parent)
        self.connected.connect(self.clientConnected)
        self.readyRead.connect(self.readReponse)
        self.disconnected.connect(self.deleteLater)
        self.error.connect(self.socketHasError)
        self.nextBlockSize = 0
        self.clientIp = ""
        # server = TcpServer object
        self.server = parent
        #print("client addr = {}".format(str(self.peerName())))

    def clientConnected(self):
        #print("client addr = {}".format(str(self.peerAddress().toString())))
        print("client connnect ...")

    # recv the message from client
    def readReponse(self):
        if self.clientIp == "":
            print("client addr = {}".format(str(self.peerAddress().toString())))
            self.clientIp = self.peerAddress().toString()
            self.server.clientConnect(self.clientIp,self)
        #print("ready to read ...")
        # print(self.bytesAvailable())
        # print(self.canReadLine())
        content = self.readLine()
        print("content = " + str(content.data(),"utf-8"))
        self.server.recvMessage(self.clientIp,str(content.data(),"utf-8").strip())

    def socketHasError(self, error):
        print("client has error = " + self.errorString())
        self.close()

class TcpServer(QTcpServer):

    def __init__(self, parent=None):
        super(TcpServer, self).__init__(parent)
        self.ui = parent
        self.clientSocketList = []
        self.clientIpList = []

    def incomingConnection(self, socketId):
        socket = TcpSocket(self)
        socket.setSocketDescriptor(socketId)

    def clientConnect(self, ipAddr, socket):
        print("tcp server client connect ...")
        self.clientIpList.append(ipAddr)
        self.clientSocketList.append(socket)
        self.ui.clientConnect(ipAddr)

    def sendMessage(self,ip,msg):
        print("sendMsg ip = " + ip + " msg = " + msg)
        index = 0
        for i in range(0,len(self.clientIpList)):
            print("ip = " + self.clientIpList[i])
            if self.clientIpList[i] == ip:
                index = i
        #index = self.clientIpList.index(ip)
        print("sendMsg ip idx = " + str(index))
        data = QByteArray()
        data.append(msg)
        data.append("\n")
        self.clientSocketList[index].write(data)

    def sendLuaMessage(self,ip,msg):
        print("sendLuaMessage ip = " + ip + " msg = " + msg)
        index = 0
        for i in range(0,len(self.clientIpList)):
            print("ip = " + self.clientIpList[i])
            if self.clientIpList[i] == ip:
                index = i
        #index = self.clientIpList.index(ip)
        print("sendMsg ip idx = " + str(index))
        data = QByteArray()
        data.append(msg)
        self.clientSocketList[index].write(data)

    def recvMessage(self,ipAddr,msg):
        self.ui.recvMessage(ipAddr,msg)
        pass

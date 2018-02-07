#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget,QMessageBox
                             ,QHBoxLayout,QVBoxLayout,QLabel,QPushButton,QWidget,QLineEdit,QInputDialog)
from PyQt5.QtCore import Qt
import socketserver
import _thread
import time

mAppExit = False
mClientList = []
mListWidget = None

class ComCoreHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        global mClientList
        global mListWidget
        print("{} wrote:".format(self.client_address[0]))
        mClientList.append(self.client_address[0])
        mListWidget.clear()
        mListWidget.addItem(self.client_address[0])
        self.data = self.rfile.readline().strip()
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
        self.addDock()


    def init(self):
        # self.text = QTextEdit('')
        # self.text.setAlignment(Qt.AlignLeft)
        # self.setCentralWidget(self.text)
        self.targetName = QLabel("1.2.3.4")
        self.targetStatus = QTextEdit('')
        self.targetCmdEdit = QTextEdit('')
        targetCmdLabel =  QLabel("Cmd : ")
        self.targetFile = QPushButton(" + ")
        self.targetSend = QPushButton("Send")
        targetBottomBox = QHBoxLayout()
        targetBottomBox.addWidget(targetCmdLabel)
        targetBottomBox.addWidget(self.targetCmdEdit)
        targetBottomBox.addWidget(self.targetFile)
        targetBottomBox.addWidget(self.targetSend)

        vbox = QVBoxLayout()
        #vbox.addWidget(self.targetName)
        #vbox.addWidget(self.targetStatus)
        vbox.addLayout(targetBottomBox)

        #self.setLayout(vbox)

        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle('Task Center Server')
        self.show()
        pass

    # deal with ListWidget current Row changed function
    def onDockListIndexChanged(self, index):
        item = self.items[index]
        self.text.setText(item)
        pass

    def addDock(self):
        global mListWidget
        clientDock = QDockWidget('Client List')
        clientDock.setFeatures(QDockWidget.DockWidgetFloatable)
        clientDock.setAllowedAreas(Qt.LeftDockWidgetArea)
        listwidget = QListWidget()
        mListWidget = listwidget

        #listwidget.addItems(self.items)
        # add current row changed listener
        listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
        clientDock.setWidget(listwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, clientDock)

    def closeEvent(self, event):
        global mAppExit
        reply = QMessageBox.question(self, 'Confirm',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            mAppExit = True
            event.accept()
        else:
            mAppExit = False
            event.ignore()

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))
def app_func(name):
    print(name, " is start ...")
    # start app ui
    app = QApplication(sys.argv)
    window = MainWindow()
    Example()
    sys.exit(app.exec_())

def socket_func(name):
    print(name," is start ...")
    HOST, PORT = "localhost", 9008
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), ComCoreHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    print("localhost socket server is listening addr: " + HOST + "port :" + str(PORT))
    sys.exit(server.serve_forever())

def main():
    global mAppExit
    print("main start ...")
    try:
        _thread.start_new_thread(app_func, ("UI-Thread",))
        _thread.start_new_thread(socket_func, ("Socket-Thread",))
    except:
        print("Error: unable to start thread")

    while 1:
        if mAppExit:
            break
        #print("main thread is waiting ...mAppExit = " + str(mAppExit))
        time.sleep(5)



# main function
if __name__ == '__main__':
    main()
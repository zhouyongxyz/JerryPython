#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz
# serverui.py

# Form implementation generated from reading ui file 'taskserver.ui'
#
# Created: Mon Feb  5 10:21:33 2018
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QWidget ,QMainWindow,QInputDialog   #导入相应的包
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout()
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.clientTreeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.clientTreeWidget.setObjectName("clientTreeWidget")
        # item_0 = QtWidgets.QTreeWidgetItem(self.clientTreeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout_main.addWidget(self.clientTreeWidget)
        self.contentTabWiget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentTabWiget.sizePolicy().hasHeightForWidth())
        self.contentTabWiget.setSizePolicy(sizePolicy)
        self.contentTabWiget.setObjectName("contentTabWiget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_content = QtWidgets.QVBoxLayout()
        self.verticalLayout_content.setObjectName("verticalLayout_content")
        self.content_ipaddr = QtWidgets.QLabel(self.tab_1)
        self.content_ipaddr.setObjectName("content_ipaddr")
        self.verticalLayout_content.addWidget(self.content_ipaddr)
        self.content_status = QtWidgets.QTextEdit(self.tab_1)
        self.content_status.setObjectName("content_status")
        self.verticalLayout_content.addWidget(self.content_status)
        self.horizontalLayout_content_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_content_2.setObjectName("horizontalLayout_content_2")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_content_2.addWidget(self.label_2)
        self.edit_cmd = QtWidgets.QLineEdit(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_cmd.sizePolicy().hasHeightForWidth())
        self.edit_cmd.setSizePolicy(sizePolicy)
        self.edit_cmd.setObjectName("edit_cmd")
        self.horizontalLayout_content_2.addWidget(self.edit_cmd)
        self.btn_file = QtWidgets.QPushButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_file.sizePolicy().hasHeightForWidth())
        self.btn_file.setSizePolicy(sizePolicy)
        self.btn_file.setObjectName("btn_file")
        self.horizontalLayout_content_2.addWidget(self.btn_file)
        self.btn_send = QtWidgets.QPushButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout_content_2.addWidget(self.btn_send)
        self.verticalLayout_content.addLayout(self.horizontalLayout_content_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_content)
        self.contentTabWiget.addTab(self.tab_1, "")

        self.horizontalLayout_main.addWidget(self.contentTabWiget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose_C = QtWidgets.QAction(MainWindow)
        self.actionClose_C.setObjectName("actionClose_C")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose_C)
        self.menuAbout.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        #add tab 2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_editor = QtWidgets.QVBoxLayout()
        self.verticalLayout_editor.setObjectName("verticalLayout_editor")
        self.horizontalLayout_editor = QtWidgets.QHBoxLayout()
        self.horizontalLayout_editor.setObjectName("horizontalLayout_editor")
        spacerItem = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_editor.addItem(spacerItem)
        self.btn_run = QtWidgets.QPushButton(self.tab_2)
        self.btn_run.setObjectName("btn_run")
        self.horizontalLayout_editor.addWidget(self.btn_run)
        self.verticalLayout_editor.addLayout(self.horizontalLayout_editor)
        self.code_editor = QtWidgets.QTextEdit(self.tab_2)
        self.code_editor.setObjectName("code_editor")
        self.verticalLayout_editor.addWidget(self.code_editor)
        self.verticalLayout_4.addLayout(self.verticalLayout_editor)
        self.contentTabWiget.addTab(self.tab_2, "")

        self.retranslateUi(MainWindow)
        self.contentTabWiget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task Server v1.0"))
        self.clientTreeWidget.headerItem().setText(0, _translate("MainWindow", "连接设备"))
        # __sortingEnabled = self.clientTreeWidget.isSortingEnabled()
        # self.clientTreeWidget.setSortingEnabled(False)
        # self.clientTreeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "网络1"))
        # self.clientTreeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "1.2.3.4"))
        # self.clientTreeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "192.168.65.65"))
        # self.clientTreeWidget.setSortingEnabled(__sortingEnabled)
        self.content_ipaddr.setText(_translate("MainWindow", " 1.2.3.4"))
        self.label_2.setText(_translate("MainWindow", "Cmd:"))
        self.btn_file.setText(_translate("MainWindow", "+"))
        self.btn_send.setText(_translate("MainWindow", "Send"))
        self.contentTabWiget.setTabText(self.contentTabWiget.indexOf(self.tab_1), _translate("MainWindow", "Status"))
        self.contentTabWiget.setTabText(self.contentTabWiget.indexOf(self.tab_2), _translate("MainWindow", "Editor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open(&O)"))
        self.actionClose_C.setText(_translate("MainWindow", "Close(&C)"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.btn_run.setText(_translate("MainWindow", "Run"))
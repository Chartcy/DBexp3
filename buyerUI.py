# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buyerUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.houseinfoTable = QtWidgets.QTableWidget(self.centralwidget)
        self.houseinfoTable.setGeometry(QtCore.QRect(10, 70, 781, 141))
        self.houseinfoTable.setObjectName("houseinfoTable")
        self.houseinfoTable.setColumnCount(0)
        self.houseinfoTable.setRowCount(0)
        self.userIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.userIdLabel.setGeometry(QtCore.QRect(150, 10, 131, 16))
        self.userIdLabel.setObjectName("userIdLabel")
        self.pwdLabel = QtWidgets.QLabel(self.centralwidget)
        self.pwdLabel.setGeometry(QtCore.QRect(360, 10, 221, 21))
        self.pwdLabel.setObjectName("pwdLabel")
        self.InfonameLabel = QtWidgets.QLabel(self.centralwidget)
        self.InfonameLabel.setGeometry(QtCore.QRect(390, 20, 91, 16))
        self.InfonameLabel.setText("")
        self.InfonameLabel.setObjectName("InfonameLabel")
        self.InfosexLabel = QtWidgets.QLabel(self.centralwidget)
        self.InfosexLabel.setGeometry(QtCore.QRect(630, 20, 72, 15))
        self.InfosexLabel.setText("")
        self.InfosexLabel.setObjectName("InfosexLabel")
        self.telLabel = QtWidgets.QLabel(self.centralwidget)
        self.telLabel.setGeometry(QtCore.QRect(150, 40, 131, 16))
        self.telLabel.setObjectName("telLabel")
        self.InfotelLabel = QtWidgets.QLabel(self.centralwidget)
        self.InfotelLabel.setGeometry(QtCore.QRect(140, 60, 151, 16))
        self.InfotelLabel.setText("")
        self.InfotelLabel.setObjectName("InfotelLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 781, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.houseIdLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.houseIdLabel.setObjectName("houseIdLabel")
        self.horizontalLayout.addWidget(self.houseIdLabel)
        self.rsvHouseID = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.rsvHouseID.setFrame(True)
        self.rsvHouseID.setObjectName("rsvHouseID")
        self.horizontalLayout.addWidget(self.rsvHouseID)
        self.addReserve = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addReserve.setObjectName("addReserve")
        self.horizontalLayout.addWidget(self.addReserve)
        self.deleteReserve = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteReserve.setObjectName("deleteReserve")
        self.horizontalLayout.addWidget(self.deleteReserve)
        self.CollectTable = QtWidgets.QTableWidget(self.centralwidget)
        self.CollectTable.setGeometry(QtCore.QRect(10, 380, 291, 191))
        self.CollectTable.setObjectName("CollectTable")
        self.CollectTable.setColumnCount(0)
        self.CollectTable.setRowCount(0)
        self.ReserveTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ReserveTable.setGeometry(QtCore.QRect(340, 380, 451, 191))
        self.ReserveTable.setObjectName("ReserveTable")
        self.ReserveTable.setColumnCount(0)
        self.ReserveTable.setRowCount(0)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 781, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.houseIdLabel_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.houseIdLabel_2.setObjectName("houseIdLabel_2")
        self.horizontalLayout_2.addWidget(self.houseIdLabel_2)
        self.colHouseID = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.colHouseID.setFrame(True)
        self.colHouseID.setObjectName("colHouseID")
        self.horizontalLayout_2.addWidget(self.colHouseID)
        self.addCollect = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addCollect.setObjectName("addCollect")
        self.horizontalLayout_2.addWidget(self.addCollect)
        self.deleteCollect = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.deleteCollect.setObjectName("deleteCollect")
        self.horizontalLayout_2.addWidget(self.deleteCollect)
        self.houseIdLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.houseIdLabel_3.setGeometry(QtCore.QRect(110, 320, 101, 31))
        self.houseIdLabel_3.setObjectName("houseIdLabel_3")
        self.watchHouseTime = QtWidgets.QLineEdit(self.centralwidget)
        self.watchHouseTime.setGeometry(QtCore.QRect(210, 320, 201, 31))
        self.watchHouseTime.setObjectName("watchHouseTime")
        self.houseIdLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.houseIdLabel_4.setGeometry(QtCore.QRect(430, 320, 101, 31))
        self.houseIdLabel_4.setObjectName("houseIdLabel_4")
        self.watchHousePeople = QtWidgets.QLineEdit(self.centralwidget)
        self.watchHousePeople.setGeometry(QtCore.QRect(530, 320, 201, 31))
        self.watchHousePeople.setObjectName("watchHousePeople")
        self.houseIdLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.houseIdLabel_5.setGeometry(QtCore.QRect(90, 30, 41, 21))
        self.houseIdLabel_5.setObjectName("houseIdLabel_5")
        self.houseIdLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.houseIdLabel_6.setGeometry(QtCore.QRect(70, 0, 61, 21))
        self.houseIdLabel_6.setObjectName("houseIdLabel_6")
        self.houseIdLabel_7 = QtWidgets.QLabel(self.centralwidget)
        self.houseIdLabel_7.setGeometry(QtCore.QRect(300, 10, 41, 21))
        self.houseIdLabel_7.setObjectName("houseIdLabel_7")
        self.houseIdLabel_8 = QtWidgets.QLabel(self.centralwidget)
        self.houseIdLabel_8.setGeometry(QtCore.QRect(10, 340, 60, 49))
        self.houseIdLabel_8.setObjectName("houseIdLabel_8")
        self.houseIdLabel_9 = QtWidgets.QLabel(self.centralwidget)
        self.houseIdLabel_9.setGeometry(QtCore.QRect(340, 340, 60, 49))
        self.houseIdLabel_9.setObjectName("houseIdLabel_9")
        self.jumpToSearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.jumpToSearchButton.setGeometry(QtCore.QRect(540, 30, 131, 31))
        self.jumpToSearchButton.setObjectName("jumpToSearchButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(690, 30, 71, 31))
        self.exitButton.setObjectName("exitButton")
        self.editUserInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.editUserInfoButton.setGeometry(QtCore.QRect(380, 30, 131, 31))
        self.editUserInfoButton.setObjectName("editUserInfoButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userIdLabel.setText(_translate("MainWindow", "用户ID"))
        self.pwdLabel.setText(_translate("MainWindow", "密码"))
        self.telLabel.setText(_translate("MainWindow", "手机"))
        self.houseIdLabel.setText(_translate("MainWindow", "房源编号"))
        self.addReserve.setText(_translate("MainWindow", "加入预约"))
        self.deleteReserve.setText(_translate("MainWindow", "取消预约"))
        self.houseIdLabel_2.setText(_translate("MainWindow", "房源编号"))
        self.addCollect.setText(_translate("MainWindow", "加入收藏"))
        self.deleteCollect.setText(_translate("MainWindow", "取消收藏"))
        self.houseIdLabel_3.setText(_translate("MainWindow", "预约看房时间"))
        self.houseIdLabel_4.setText(_translate("MainWindow", "预约看房人数"))
        self.houseIdLabel_5.setText(_translate("MainWindow", "手机："))
        self.houseIdLabel_6.setText(_translate("MainWindow", "用户ID："))
        self.houseIdLabel_7.setText(_translate("MainWindow", "密码："))
        self.houseIdLabel_8.setText(_translate("MainWindow", "收藏表："))
        self.houseIdLabel_9.setText(_translate("MainWindow", "预约表："))
        self.jumpToSearchButton.setText(_translate("MainWindow", "跳转到查询界面"))
        self.exitButton.setText(_translate("MainWindow", "退出"))
        self.editUserInfoButton.setText(_translate("MainWindow", "编辑用户信息"))

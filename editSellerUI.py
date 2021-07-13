# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editSellerUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 399)
        self.newName = QtWidgets.QLineEdit(Form)
        self.newName.setGeometry(QtCore.QRect(160, 60, 171, 21))
        self.newName.setObjectName("newName")
        self.newPsw = QtWidgets.QLineEdit(Form)
        self.newPsw.setGeometry(QtCore.QRect(160, 100, 171, 21))
        self.newPsw.setObjectName("newPsw")
        self.nolabel = QtWidgets.QLabel(Form)
        self.nolabel.setGeometry(QtCore.QRect(180, 20, 141, 21))
        self.nolabel.setObjectName("nolabel")
        self.pwdlabel = QtWidgets.QLabel(Form)
        self.pwdlabel.setGeometry(QtCore.QRect(90, 60, 72, 15))
        self.pwdlabel.setObjectName("pwdlabel")
        self.modifyButton = QtWidgets.QPushButton(Form)
        self.modifyButton.setGeometry(QtCore.QRect(120, 330, 93, 28))
        self.modifyButton.setObjectName("modifyButton")
        self.pwdlabel_2 = QtWidgets.QLabel(Form)
        self.pwdlabel_2.setGeometry(QtCore.QRect(90, 100, 72, 15))
        self.pwdlabel_2.setObjectName("pwdlabel_2")
        self.returnButton = QtWidgets.QPushButton(Form)
        self.returnButton.setGeometry(QtCore.QRect(280, 330, 93, 28))
        self.returnButton.setObjectName("returnButton")
        self.pwdlabel_3 = QtWidgets.QLabel(Form)
        self.pwdlabel_3.setGeometry(QtCore.QRect(70, 150, 71, 16))
        self.pwdlabel_3.setObjectName("pwdlabel_3")
        self.newAgency = QtWidgets.QLineEdit(Form)
        self.newAgency.setGeometry(QtCore.QRect(160, 150, 171, 21))
        self.newAgency.setObjectName("newAgency")
        self.pwdlabel_4 = QtWidgets.QLabel(Form)
        self.pwdlabel_4.setGeometry(QtCore.QRect(71, 200, 91, 20))
        self.pwdlabel_4.setObjectName("pwdlabel_4")
        self.newWorkYear = QtWidgets.QLineEdit(Form)
        self.newWorkYear.setGeometry(QtCore.QRect(160, 200, 171, 21))
        self.newWorkYear.setObjectName("newWorkYear")
        self.pwdlabel_5 = QtWidgets.QLabel(Form)
        self.pwdlabel_5.setGeometry(QtCore.QRect(100, 250, 51, 16))
        self.pwdlabel_5.setObjectName("pwdlabel_5")
        self.newCommission = QtWidgets.QLineEdit(Form)
        self.newCommission.setGeometry(QtCore.QRect(160, 250, 171, 21))
        self.newCommission.setObjectName("newCommission")
        self.nolabel_2 = QtWidgets.QLabel(Form)
        self.nolabel_2.setGeometry(QtCore.QRect(110, 290, 261, 21))
        self.nolabel_2.setObjectName("nolabel_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nolabel.setText(_translate("Form", "经纪人ID不可修改"))
        self.pwdlabel.setText(_translate("Form", "新名字："))
        self.modifyButton.setText(_translate("Form", "确认修改"))
        self.pwdlabel_2.setText(_translate("Form", "新密码："))
        self.returnButton.setText(_translate("Form", "返回"))
        self.pwdlabel_3.setText(_translate("Form", "新机构ID："))
        self.pwdlabel_4.setText(_translate("Form", "工作年限："))
        self.pwdlabel_5.setText(_translate("Form", "佣金："))
        self.nolabel_2.setText(_translate("Form", "评分不可自己修改，网站用户进行打分"))


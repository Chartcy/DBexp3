from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 203)
        self.newPsw = QtWidgets.QLineEdit(Form)
        self.newPsw.setGeometry(QtCore.QRect(160, 60, 171, 21))
        self.newPsw.setObjectName("newPsw")
        self.newTel = QtWidgets.QLineEdit(Form)
        self.newTel.setGeometry(QtCore.QRect(160, 100, 171, 21))
        self.newTel.setObjectName("newTel")
        self.nolabel = QtWidgets.QLabel(Form)
        self.nolabel.setGeometry(QtCore.QRect(180, 20, 121, 21))
        self.nolabel.setObjectName("nolabel")
        self.pwdlabel = QtWidgets.QLabel(Form)
        self.pwdlabel.setGeometry(QtCore.QRect(90, 60, 72, 15))
        self.pwdlabel.setObjectName("pwdlabel")
        self.modifyButton = QtWidgets.QPushButton(Form)
        self.modifyButton.setGeometry(QtCore.QRect(120, 150, 93, 28))
        self.modifyButton.setObjectName("modifyButton")
        self.pwdlabel_2 = QtWidgets.QLabel(Form)
        self.pwdlabel_2.setGeometry(QtCore.QRect(90, 100, 72, 15))
        self.pwdlabel_2.setObjectName("pwdlabel_2")
        self.returnButton = QtWidgets.QPushButton(Form)
        self.returnButton.setGeometry(QtCore.QRect(240, 150, 93, 28))
        self.returnButton.setObjectName("returnButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nolabel.setText(_translate("Form", "用户ID不可修改"))
        self.pwdlabel.setText(_translate("Form", "新密码："))
        self.modifyButton.setText(_translate("Form", "确认修改"))
        self.pwdlabel_2.setText(_translate("Form", "新电话："))
        self.returnButton.setText(_translate("Form", "返回"))


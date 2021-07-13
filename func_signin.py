import sys
from PyQt5 import QtWidgets
from login import Ui_Form
from func_buyer import buyerUI
from func_seller import sellerUI


class LogIn(QtWidgets.QWidget, Ui_Form):

    def __init__(self, db, cursor):
        super(LogIn, self).__init__()
        self.setupUi(self)

        self.sql = ''
        self.db = db
        self.cursor = cursor

        self.loginpushButton.clicked.connect(self.login)
        self.signUpButton.clicked.connect(self.signUpFun)

    def login(self):
        if self.usernoline.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', 'ID不能为空！')

        if self.buyerButton.isChecked() == False and self.sellerButton.isChecked() == False :
            QtWidgets.QMessageBox.warning(self, 'Warning', '必须勾选一项角色身份！')

        if self.buyerButton.isChecked():
            self.sql = 'select user_ID, psw from user where user_ID = \"' + self.usernoline.text() \
                       + "\" ;"
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            print(self.data)
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '不存在该买家账户，请注册！')
                self.usernoline.clear()
                self.pwdline.clear()
            elif self.data[1] == self.pwdline.text():
                self.hide()
                self.buyerUI = buyerUI(self,self.db, self.cursor, self.data[0])
                self.buyerUI.show()
            else:
                QtWidgets.QMessageBox.warning(self, 'Warning', '密码错误')

        elif self.sellerButton.isChecked():
            self.sql = 'select agentID, agentPwd from agent where agentID = \"' + self.usernoline.text() \
                       + "\" ;"
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '不存在该经纪人账户，请注册！')
                self.usernoline.clear()
            elif self.data[1] == self.pwdline.text():
                self.close()
                print("成功匹配seller的密码")
                self.sellerUI = sellerUI(self,self.db, self.cursor, self.data[0])
                print("成功调用sellerUI")
                self.sellerUI.show()
            else:
                QtWidgets.QMessageBox.warning(self, 'Warning', '密码错误')
        else:
            pass

    def signUpFun(self):
        if self.usernoline.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', 'ID不能为空！')
        if self.pwdline.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '密码不能为空！')
        if self.buyerButton.isChecked() == False and self.sellerButton.isChecked() == False :
            QtWidgets.QMessageBox.warning(self, 'Warning', '必须勾选一项角色身份！')

        self.sql = 'select * from agent where agentID = \"' + self.usernoline.text() \
                   + "\" ;"
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchone()
        if self.data is not None:
            QtWidgets.QMessageBox.warning(self, 'Warning', '该账户已存在，请重新设置ID（U+数字）！')
            self.usernoline.clear()
        else:
            if self.buyerButton.isChecked():
                self.sql = 'insert into user(user_Id,psw,userTel) values(\"'+self.usernoline.text()+'\",\"'+self.pwdline.text()+'\",\"'+str(00000000000)+'\");'
                self.cursor.execute(self.sql)
                QtWidgets.QMessageBox.warning(self, 'Warning', '注册成功，请重新登录！')
                self.usernoline.clear()
                self.pwdline.clear()
            elif self.sellerButton.isChecked():
                self.sql = 'insert into agent(agentId,agentName,agentPwd,agencyID,workYear,commission,agentScore) \
                    values(\"' + self.usernoline.text() + '\",' + '\"XXX\"' + ',\"'+ self.pwdline.text() + '\",\"'  \
                           + 'Agc000' + '\",\"'+ '0' +'\",\"' +'0'+'\",\"'+'0' +'\");'
                self.cursor.execute(self.sql)
                QtWidgets.QMessageBox.warning(self, 'Warning', '注册成功，请重新登录！')
                self.usernoline.clear()
                self.pwdline.clear()
            else:
                pass

def showLoginUI(db, cursor):
    app = QtWidgets.QApplication(sys.argv)
    loginUI = LogIn(db, cursor)
    loginUI.show()
    sys.exit(app.exec_())

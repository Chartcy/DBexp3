import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from editUserUI import Ui_Form

class editUserUI(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent_gui,db, cursor, user_ID):
        super(editUserUI, self).__init__()
        self.setupUi(self)

        self.db = db
        self.cursor = cursor
        self.buyer_no = user_ID
        self.parent_gui = parent_gui

        self.modifyButton.clicked.connect(self.modifyFun)
        self.returnButton.clicked.connect(self.returnFun)

    def modifyFun(self):
        if self.newPsw.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '密码不能为空！')
        elif self.newTel.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '电话不能为空！')
        else:
            self.sql = 'update user set psw =\"' + self.newPsw.text() + '\", userTel=\"'+self.newTel.text()+'\" where user_ID = \"' \
                + self.buyer_no + '\";'
            self.cursor.execute(self.sql)
            QtWidgets.QMessageBox.warning(self, 'Warning', '修改完成！')
            self.newPsw.clear()
            self.newTel.clear()

    def returnFun(self):
        self.close()
        self.parent_gui.show()
        self.parent_gui.showUserInfo()







if __name__ == "__main__":
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="exp3")
    cursor = db.cursor()
    app = QtWidgets.QApplication(sys.argv)
    print("sys.argv")
    print(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    buyerUI = editUserUI(db, cursor, "U001")
    buyerUI.show()
    sys.exit(app.exec_())

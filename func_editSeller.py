import pymysql
import sys
from PyQt5 import QtWidgets
from editSellerUI import Ui_Form

class editSellerUI(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent_gui,db, cursor, agentID):
        super(editSellerUI, self).__init__()
        self.setupUi(self)

        self.db = db
        self.cursor = cursor
        self.seller_no = agentID
        self.parent_gui = parent_gui

        self.modifyButton.clicked.connect(self.modifyFun)
        self.returnButton.clicked.connect(self.returnFun)

    def modifyFun(self):
        if self.newName.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '新名字不能为空！')
        elif self.newPsw.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '新密码不能为空！')
        elif self.newAgency.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '新机构不能为空！')
        elif self.newWorkYear.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '工作年限不能为空！')
        elif self.newCommission.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '佣金不能为空！')

        else:
            self.sql = 'update agent set agentName =\"' + self.newName.text() +  \
                       '\", agencyID=\"'+self.newAgency.text()+ \
                       '\", workYear=\"' + self.newWorkYear.text() + \
                       '\", commission=\"' + self.newCommission.text() + \
                       '\" where agentID = \"' \
                        + self.seller_no + '\";'
            self.cursor.execute(self.sql)
            QtWidgets.QMessageBox.warning(self, 'Warning', '修改完成！')
            self.newName.clear()
            self.newPsw.clear()
            self.newAgency.clear()
            self.newWorkYear.clear()
            self.newCommission.clear()


    def returnFun(self):
        self.close()
        self.parent_gui.show()
        self.parent_gui.showAgentInfo()







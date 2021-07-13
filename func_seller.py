import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from sellerUI import Ui_MainWindow
from func_search import searchUI
from func_editSeller import editSellerUI

class sellerUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent_gui,db, cursor, agentID):
        super(sellerUI, self).__init__()
        self.setupUi(self)

        self.db = db
        self.cursor = cursor
        self.seller_no = agentID
        self.parent_gui = parent_gui

        self.agentHouseTable.setColumnCount(7)
        self.agentHouseTable.setHorizontalHeaderLabels(["房源编号", "类型编号", "面积", "朝向", "楼层", "价格", "小区"])
        self.agentHouseTable.resizeRowsToContents()

        self.agentHouseTable.setColumnWidth(0, 90)
        self.agentHouseTable.setColumnWidth(1, 90)
        self.agentHouseTable.setColumnWidth(2, 70)
        self.agentHouseTable.setColumnWidth(3, 70)
        self.agentHouseTable.setColumnWidth(4, 50)
        self.agentHouseTable.setColumnWidth(5, 70)
        self.agentHouseTable.setColumnWidth(6, 90)

        self.allHouseInfoTable.setColumnCount(9)
        self.allHouseInfoTable.setHorizontalHeaderLabels(["房源编号", "类型编号", "面积", "朝向", "楼层", "价格", "小区", "经纪人", "中介机构"])
        self.allHouseInfoTable.resizeRowsToContents()
        self.allHouseInfoTable.setColumnWidth(0, 90)
        self.allHouseInfoTable.setColumnWidth(1, 90)
        self.allHouseInfoTable.setColumnWidth(2, 70)
        self.allHouseInfoTable.setColumnWidth(3, 70)
        self.allHouseInfoTable.setColumnWidth(4, 50)
        self.allHouseInfoTable.setColumnWidth(5, 70)
        self.allHouseInfoTable.setColumnWidth(6, 90)
        self.allHouseInfoTable.setColumnWidth(7, 90)
        self.allHouseInfoTable.setColumnWidth(8, 90)

        self.showAgentInfo()
        self.setagentHouseTable()
        self.setallHouseInfoTable()

        self.modifyButton.clicked.connect(self.modifyHouseInfo)
        self.deleteButton.clicked.connect(self.deleteHouseInfo)
        self.addButton.clicked.connect(self.addHouseInfo)
        self.jumpToSearchButton.clicked.connect(self.jumpToSearchFun)
        self.exitButton.clicked.connect(self.exitFun)
        self.editSellerButton.clicked.connect(self.jumpToEditSellerFun)

    def jumpToSearchFun(self):
        self.hide()
        self.searchUI = searchUI(self, self.db, self.cursor)
        self.searchUI.show()

    def exitFun(self):
        self.close()
        self.parent_gui.show()

    def jumpToEditSellerFun(self):
        self.hide()
        self.editSellerUI = editSellerUI(self, self.db, self.cursor,self.seller_no)
        self.editSellerUI.show()

    def showAgentInfo(self):
        print("show agent info")
        self.sql = 'select agentID, agentName, agentPwd, agencyID, workYear, agentScore, commission from agent where agentID = \"' \
                   + self.seller_no + '\";'
        print("select agent info sucessfully!")
        self.cursor.execute(self.sql)
        self.sellerInfo = self.cursor.fetchone()

        self.agentIdInfo.setText(self.sellerInfo[0])
        self.agentNameInfo.setText(self.sellerInfo[1])
        self.agentPswInfo.setText(str(self.sellerInfo[2]))
        self.agencyIdInfo.setText(str(self.sellerInfo[3]))
        self.workYearInfo.setText(str(self.sellerInfo[4]))
        self.agentScoreInfo.setText(str(self.sellerInfo[5]))
        self.agentCommissionInfo.setText(str(self.sellerInfo[6]))
        print("set agent info sucessfully!")


    def dataToAgentHouseTable(self, data):
        self.agentHouseTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 7):
                self.agentHouseTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setagentHouseTable(self):
        self.sql = 'select houseID,typeID,area,towards,floor,price,communityID from house where agentID = \"' \
                   + self.seller_no + '\";'
        self.cursor.execute(self.sql)
        self.houseInfo = self.cursor.fetchall()
        self.dataToAgentHouseTable(self.houseInfo)

    def dataToAllHouseInfoTable(self, data):
        self.allHouseInfoTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 9):
                self.allHouseInfoTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setallHouseInfoTable(self):
        self.sql = 'select * from house'
        self.cursor.execute(self.sql)
        self.allhouseInfo = self.cursor.fetchall()
        self.dataToAllHouseInfoTable(self.allhouseInfo)

    def modifyHouseInfo(self):
        if self.modifyHouseID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '房源编号不能为空！')

        elif self.chooseSquare.isChecked() == False \
                and self.chooseTowards.isChecked() == False \
                and self.chooseFloor.isChecked() == False \
                and self.choosePrice.isChecked() == False \
                and self.chooseCommunity.isChecked() == False :
            QtWidgets.QMessageBox.warning(self, 'Warning', '必须勾选一项需要修改的信息！')

        elif self.modifyContent.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '修改的内容不能为空！')

        else:
            self.sql = 'select * from house where agentID =\"' + self.seller_no + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该经纪人并不代理此编号的房源！')
            else:
                if self.chooseSquare.isChecked() == True:
                    self.sql = 'update house set area = \"' + self.modifyContent.text() + '\"where houseID =\"' + self.modifyHouseID.text() + '\";'
                    print(self.sql)
                    self.cursor.execute(self.sql)
                    QtWidgets.QMessageBox.information(self, 'Information', '已修改此房屋面积信息')

                elif self.chooseTowards.isChecked() == True:
                    self.sql = 'update house set towards = \"' + self.modifyContent.text() + '\"where houseID =\"' + self.modifyHouseID.text() + '\";'
                    print(self.sql)
                    self.cursor.execute(self.sql)
                    QtWidgets.QMessageBox.information(self, 'Information', '已修改此房屋朝向信息')

                elif self.chooseFloor.isChecked() == True:
                    self.sql = 'update house set floor = \"' + self.modifyContent.text() + '\"where houseID =\"' + self.modifyHouseID.text() + '\";'
                    print(self.sql)
                    self.cursor.execute(self.sql)
                    QtWidgets.QMessageBox.information(self, 'Information', '已修改此房屋楼层信息')

                elif self.choosePrice.isChecked() == True:
                    self.sql = 'update house set price = \"' + self.modifyContent.text() + '\"where houseID =\"' + self.modifyHouseID.text() + '\";'
                    print(self.sql)
                    self.cursor.execute(self.sql)
                    QtWidgets.QMessageBox.information(self, 'Information', '已修改此房屋价格信息')

                elif self.chooseCommunity.isChecked() == True:
                    self.sql = 'update house set community = \"' + self.modifyContent.text() + '\"where houseID =\"' + self.modifyHouseID.text() + '\";'
                    print(self.sql)
                    self.cursor.execute(self.sql)
                    QtWidgets.QMessageBox.information(self, 'Information', '已修改此房屋所在社区信息')

                else:
                    pass

                self.db.commit()
                self.setagentHouseTable()
                self.setallHouseInfoTable()
                self.modifyContent.clear()
                self.modifyHouseID.clear()

    def deleteHouseInfo(self):
        if self.deleteHouseID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '房源编号不能为空！')
        else:
            self.sql = 'select * from house where agentID =\"' + self.seller_no + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该经纪人并不代理此编号的房源，无需删除！')
            else:
                self.sql = 'update house set agentID = \"Agt000\" where houseID = \"'  + self.deleteHouseID.text() + '\";'
                print(self.sql)
                self.cursor.execute(self.sql)
                QtWidgets.QMessageBox.information(self, 'Information', '该经纪人已不再代理此房源，设置此房源经纪人为默认值Agt000！')
                self.db.commit()
                self.setagentHouseTable()
                self.setallHouseInfoTable()
                self.deleteHouseID.clear()

    def addHouseInfo(self):
        if self.addHouseID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '房源编号不能为空！')
        else:
            self.sql = 'select * from house where agentID =\"' + self.seller_no + '\"and houseID =\"' + self.addHouseID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is not None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该房源已存在！')
            else:
                self.sql = 'update house set agentID =\"' + self.seller_no + '\"where houseID = \"' + self.addHouseID.text() + '\";'
                print(self.sql)
                self.cursor.execute(self.sql)
                QtWidgets.QMessageBox.information(self, 'Information', '该房源已设置为此经纪人代理！')
                self.db.commit()
                self.setagentHouseTable()
                self.setallHouseInfoTable()
                self.addHouseID.clear()


if __name__ == "__main__":
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="exp3")
    cursor = db.cursor()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    sellerUI = sellerUI(db, cursor, "Agt001")
    sellerUI.show()
    sys.exit(app.exec_())

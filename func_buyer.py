import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from buyerUI import Ui_MainWindow
from datetime import datetime
from func_search import searchUI
from func_editUser import editUserUI

class buyerUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent_gui,db, cursor, user_ID):
        super(buyerUI, self).__init__()
        self.setupUi(self)

        self.db = db
        self.cursor = cursor
        self.buyer_no = user_ID
        self.parent_gui = parent_gui

        self.houseinfoTable.setColumnCount(9)
        self.houseinfoTable.setHorizontalHeaderLabels(["房源编号", "类型编号", "面积", "朝向", "楼层", "价格","小区","经纪人","中介机构"])
        self.houseinfoTable.resizeRowsToContents()
        #self.houseinfoTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.houseinfoTable.setColumnWidth(0, 90)
        self.houseinfoTable.setColumnWidth(1, 90)
        self.houseinfoTable.setColumnWidth(2, 70)
        self.houseinfoTable.setColumnWidth(3, 70)
        self.houseinfoTable.setColumnWidth(4, 50)
        self.houseinfoTable.setColumnWidth(5, 70)
        self.houseinfoTable.setColumnWidth(6, 90)
        self.houseinfoTable.setColumnWidth(7, 90)
        self.houseinfoTable.setColumnWidth(8, 90)

        self.CollectTable.setColumnCount(2)
        self.CollectTable.setHorizontalHeaderLabels(["房源编号", "收藏时间"])
        self.CollectTable.resizeRowsToContents()
        #self.CollectTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.CollectTable.setColumnWidth(0, 90)
        self.CollectTable.setColumnWidth(1, 90)

        self.ReserveTable.setColumnCount(3)
        self.ReserveTable.setHorizontalHeaderLabels(["房源编号", "预定时间","参观人数"])
        self.ReserveTable.resizeRowsToContents()
        #self.ReserveTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ReserveTable.setColumnWidth(0, 90)
        self.ReserveTable.setColumnWidth(1, 90)
        self.ReserveTable.setColumnWidth(2, 90)

        self.showUserInfo()
        self.setHouseTable()
        self.setCollectTable()
        self.setReserveTable()
        try:
            self.addCollect.clicked.connect(self.addCollectFun)
            self.deleteCollect.clicked.connect(self.deleteCollectFun)
            #self.updateCollect.clicked.connect(self.setCollectTable)

            self.addReserve.clicked.connect(self.addReserveFun)
            self.deleteReserve.clicked.connect(self.deleteReserveFun)
            #self.updateReserve.clicked.connect(self.setReserveTable)

            self.exitButton.clicked.connect(self.exitFun)
            self.jumpToSearchButton.clicked.connect(self.jumpToSearchFun)
            self.editUserInfoButton.clicked.connect(self.jumpToEditUserFun)

        except Exception as e:
            print(e)

    def exitFun(self):
        self.close()
        self.parent_gui.show()

    def jumpToSearchFun(self):
        self.hide()
        self.searchUI = searchUI(self,self.db, self.cursor)
        self.searchUI.show()

    def jumpToEditUserFun(self):
        self.hide()
        self.editUserUI = editUserUI(self, self.db, self.cursor,self.buyer_no)
        self.editUserUI.show()



    def showUserInfo(self):
        print("show user info")
        self.sql = 'select user_ID, psw, userTel from user where user_ID = \"' \
                   + self.buyer_no + '\";'
        print("select user info sucessfully!")
        self.cursor.execute(self.sql)
        self.buyerInfo = self.cursor.fetchone()
        print("start print")
        print(self.buyerInfo)
        self.userIdLabel.setText(self.buyerInfo[0])
        self.pwdLabel.setText(self.buyerInfo[1])
        self.telLabel.setText(str(self.buyerInfo[2]))
        #self.mailLabel.setText(self.buyerInfo[3])
        print("set user info sucessfully!")


    def dataToHouseTable(self, data):
        self.houseinfoTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 9):
                self.houseinfoTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setHouseTable(self):
        self.sql = 'select * from house;'
        self.cursor.execute(self.sql)
        self.houseInfo = self.cursor.fetchall()
        self.dataToHouseTable(self.houseInfo)

    def dataToCollectTable(self, data):
        self.CollectTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 2):
                self.CollectTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setCollectTable(self):
        self.sql = 'select collect.houseID, collect.collectTime from collect where collect.user_ID = \"' \
                   + self.buyer_no + '\";'
        print(self.sql)
        self.cursor.execute(self.sql)
        self.collectInfo = self.cursor.fetchall()
        self.dataToCollectTable(self.collectInfo)

    def dataToReserveTable(self, data):
        self.ReserveTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 3):
                self.ReserveTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setReserveTable(self):
        self.sql = 'select reserve.houseID, reserve.reserveTime, reserve.peopleNum from reserve where reserve.user_ID = \"' \
                   + self.buyer_no + '\";'
        print(self.sql)
        self.cursor.execute(self.sql)
        self.reserveInfo = self.cursor.fetchall()
        print(self.reserveInfo)
        self.dataToReserveTable(self.reserveInfo)



    def addCollectFun(self):
        try:
            if self.colHouseID.text() == '':
                QtWidgets.QMessageBox.warning(self, 'Warning', '房源编号不能为空！')
            else:
                self.sql = 'select * from collect where houseID =\"' + self.colHouseID.text() + '\";'
                print(self.sql)
                self.cursor.execute(self.sql)
                self.data = self.cursor.fetchone()
                if self.data is not None:
                    QtWidgets.QMessageBox.warning(self, 'Warning', '收藏表已存在该房源编号，请睁大眼睛！')
                else:
                    # localtime = time.asctime( time.localtime(time.time()) )
                    self.now = datetime.now()
                    self.send_time = self.now.strftime("%Y-%m-%d %H:%M:%S")
                    self.sql = 'insert into collect values (\"' + self.buyer_no + '\",\"' + self.colHouseID.text()  + '\", \"' + self.send_time + '\");'
                    print(self.sql)
                    self.cursor.execute(self.sql)
                    QtWidgets.QMessageBox.information(self, 'Information', '已加入收藏表')
                    self.db.commit()
                    self.setCollectTable()
                    self.colHouseID.clear()
        except Exception as e:
            #QtWidgets.QMessageBox.warning(self, 'Warning', '不存在该房源')
            print(e)


    def addReserveFun(self):
        #try:
            if self.rsvHouseID.text() == '' or self.watchHouseTime.text()=='' or self.watchHousePeople.text()=='':
                QtWidgets.QMessageBox.warning(self, 'Warning', '房源编号or看房时间or看房人数 不能为空！')
            else:
                self.sql = 'select * from reserve where houseID =\"' + self.rsvHouseID.text() + '\";'
                print(self.sql)
                self.cursor.execute(self.sql)
                self.data = self.cursor.fetchone()
                if self.data is not None:
                    QtWidgets.QMessageBox.warning(self, 'Warning', '预约表已存在该房源编号，请睁大眼睛！')
                else:
                    self.sql = 'insert into reserve values (\"'+self.buyer_no+'\",\"'+self.rsvHouseID.text() +'\",\"'+ self.watchHouseTime.text() \
                               + '\", ' + self.watchHousePeople.text() + ');'
                    print(self.sql)
                    self.cursor.execute(self.sql)
                    QtWidgets.QMessageBox.information(self, 'Information', '已加入预约表')
                    self.db.commit()
                    self.setReserveTable()
                    self.rsvHouseID.clear()
        #except Exception as e:
         #   QtWidgets.QMessageBox.warning(self, 'Warning', '不存在该房源')


    def deleteCollectFun(self):
        if self.colHouseID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '房源编号不能为空！')
        else:
            self.sql = 'select * from collect where houseID =\"' + self.colHouseID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '收藏表中不存在该房源！')
            else:
                self.sql = 'delete from collect where houseID= \"' + self.colHouseID.text() + '\";'
                print(self.sql)
                self.cursor.execute(self.sql)
                QtWidgets.QMessageBox.information(self, 'Information', '已从收藏表中删除')
                self.db.commit()
                self.setCollectTable()
                self.colHouseID.clear()

    def deleteReserveFun(self):
        if self.rsvHouseID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '房源编号不能为空！')
        else:
            self.sql = 'select * from reserve where houseID =\"' + self.rsvHouseID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '预约表中不存在该房源！')
            else:
                self.sql = 'delete from reserve where houseID= \"' + self.rsvHouseID.text() + '\";'
                print(self.sql)
                self.cursor.execute(self.sql)
                QtWidgets.QMessageBox.information(self, 'Information', '已从预约表中删除')
                self.db.commit()
                self.setReserveTable()
                self.rsvHouseID.clear()








if __name__ == "__main__":
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="exp3")
    cursor = db.cursor()
    print(11111111)
    app = QtWidgets.QApplication(sys.argv)
    print("sys.argv")
    print(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    buyerUI = buyerUI(db, cursor, "U001")
    buyerUI.show()
    sys.exit(app.exec_())

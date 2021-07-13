import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from searchUI import Ui_MainWindow


class searchUI(QtWidgets.QMainWindow, Ui_MainWindow):
    #def __init__(self, db, cursor, admin_no):
    def __init__(self, parent_gui,db, cursor):
        super(searchUI, self).__init__()
        self.setupUi(self)

        self.db = db
        self.cursor = cursor
        self.parent_gui = parent_gui
        #self.admin_no = admin_no

        self.agentTable.setColumnCount(6)
        self.agentTable.setHorizontalHeaderLabels(["ID", "Name", "所属中介机构", "工作年限","佣金","评分"])
        self.agentTable.resizeRowsToContents()
        self.agentTable.setColumnWidth(0, 70)
        self.agentTable.setColumnWidth(1, 90)
        self.agentTable.setColumnWidth(2, 200)
        self.agentTable.setColumnWidth(3, 100)
        self.agentTable.setColumnWidth(4, 70)
        self.agentTable.setColumnWidth(5, 50)

        self.agencyTable.setColumnCount(5)
        self.agencyTable.setHorizontalHeaderLabels(["ID", "Name", "评分", "地址","传真"])
        self.agencyTable.resizeRowsToContents()
        self.agencyTable.setColumnWidth(0, 70)
        self.agencyTable.setColumnWidth(1, 100)
        self.agencyTable.setColumnWidth(2, 50)
        self.agencyTable.setColumnWidth(3, 100)

        self.communityTable.setColumnCount(8)
        self.communityTable.setHorizontalHeaderLabels(["ID", "Name", "平均价格", "位置", "物业", "小区面积", "绿化面积", "剩余停车位"])
        self.communityTable.resizeRowsToContents()
        self.communityTable.setColumnWidth(0, 70)
        self.communityTable.setColumnWidth(1, 90)
        self.communityTable.setColumnWidth(2, 100)
        self.communityTable.setColumnWidth(3, 200)
        self.communityTable.setColumnWidth(4, 90)
        self.communityTable.setColumnWidth(5, 100)
        self.communityTable.setColumnWidth(6, 100)
        self.communityTable.setColumnWidth(7, 100)

        self.propertyTable.setColumnCount(5)
        self.propertyTable.setHorizontalHeaderLabels(["ID", "Name", "评分", "电话", "地址"])
        self.propertyTable.resizeRowsToContents()
        self.propertyTable.setColumnWidth(0, 70)
        self.propertyTable.setColumnWidth(1, 90)
        self.propertyTable.setColumnWidth(2, 50)
        self.propertyTable.setColumnWidth(3, 150)
        self.propertyTable.setColumnWidth(4, 200)

        self.houseTypeTable.setColumnCount(2)
        self.houseTypeTable.setHorizontalHeaderLabels(["ID", "类型"])
        self.houseTypeTable.resizeRowsToContents()
        self.houseTypeTable.setColumnWidth(0, 70)
        self.houseTypeTable.setColumnWidth(1, 100)

        self.returnButton.clicked.connect(self.returnFun)
        self.showOneAgent.clicked.connect(self.setoneAgentTable)
        self.showAllAgent.clicked.connect(self.setallAgentTable)
        self.showOneAgency.clicked.connect(self.setoneAgencyTable)
        self.showAllAgency.clicked.connect(self.setallAgencyTable)
        self.showOneCommunity.clicked.connect(self.setoneCommunityTable)
        self.showAllCommunity.clicked.connect(self.setallCommunityTable)
        self.showOneProperty.clicked.connect(self.setonePropertyTable)
        self.showAllProperty.clicked.connect(self.setallPropertyTable)
        self.showOneType.clicked.connect(self.setoneHouseTypeTable)
        self.showAllType.clicked.connect(self.setallHouseTypeTable)

    def returnFun(self):
        self.close()
        self.parent_gui.show()

    def dataToAgentTable(self, data):
        self.agentTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 6):
                self.agentTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setoneAgentTable(self):
        if self.searchAgentID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '经纪人编号不能为空！')
        else:
            self.sql = 'select * from agent where agentID =\"' + self.searchAgentID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该经纪人并不存在！')
            else:
                self.sql = 'select agentID,agentName,agencyID,workYear,commission,agentScore from agent where agentID = \"' + self.searchAgentID.text() + '\";'
                self.cursor.execute(self.sql)
                self.agentInfo = self.cursor.fetchall()
                self.dataToAgentTable(self.agentInfo)

    def setallAgentTable(self):
        self.sql = 'select agentID,agentName,agencyID,workYear,commission,agentScore from agent;'
        self.cursor.execute(self.sql)
        self.agentInfo = self.cursor.fetchall()
        self.dataToAgentTable(self.agentInfo)

    def dataToAgencyTable(self, data):
        self.agencyTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 5):
                self.agencyTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setallAgencyTable(self):
        self.sql = 'select * from agency;'
        self.cursor.execute(self.sql)
        self.agencyInfo = self.cursor.fetchall()
        self.dataToAgencyTable(self.agencyInfo)

    def setoneAgencyTable(self):
        if self.searchAgencyID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '机构编号不能为空！')
        else:
            self.sql = 'select * from agency where agencyID =\"' + self.searchAgencyID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该机构并不存在！')
            else:
                self.sql = 'select * from agency where agencyID = \"' + self.searchAgencyID.text() + '\";'
                self.cursor.execute(self.sql)
                self.agencyInfo = self.cursor.fetchall()
                self.dataToAgencyTable(self.agencyInfo)


    def dataToCommunityTable(self, data):
        self.communityTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 8):
                self.communityTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setallCommunityTable(self):
        self.sql = 'select * from community;'
        self.cursor.execute(self.sql)
        self.communityInfo = self.cursor.fetchall()
        self.dataToCommunityTable(self.communityInfo)

    def setoneCommunityTable(self):
        if self.searchCommunityID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '小区编号不能为空！')
        else:
            self.sql = 'select * from community where communityID =\"' + self.searchCommunityID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该小区并不存在！')
            else:
                self.sql = 'select * from community where communityID = \"' + self.searchCommunityID.text() + '\";'
                self.cursor.execute(self.sql)
                self.communityInfo = self.cursor.fetchall()
                self.dataToCommunityTable(self.communityInfo)

    def dataToPropertyTable(self, data):
        self.propertyTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 5):
                self.propertyTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setallPropertyTable(self):
        self.sql = 'select * from property;'
        self.cursor.execute(self.sql)
        self.propertyInfo = self.cursor.fetchall()
        self.dataToPropertyTable(self.propertyInfo)

    def setonePropertyTable(self):
        if self.searchPropertyID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '物业编号不能为空！')
        else:
            self.sql = 'select * from property where propertyID =\"' + self.searchPropertyID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该物业并不存在！')
            else:
                self.sql = 'select * from property where propertyID = \"' + self.searchPropertyID.text() + '\";'
                self.cursor.execute(self.sql)
                self.propertyInfo = self.cursor.fetchall()
                self.dataToPropertyTable(self.propertyInfo)

    def dataToHouseTypeTable(self, data):
        self.houseTypeTable.setRowCount(len(data))
        for i in range(0, len(data)):
            for j in range(0, 2):
                self.houseTypeTable.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def setallHouseTypeTable(self):
        self.sql = 'select * from housetype;'
        self.cursor.execute(self.sql)
        self.houseTypeInfo = self.cursor.fetchall()
        self.dataToHouseTypeTable(self.houseTypeInfo)

    def setoneHouseTypeTable(self):
        if self.searchHouseTypeID.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '房屋类型编号不能为空！')
        else:
            self.sql = 'select * from housetype where typeID =\"' + self.searchHouseTypeID.text() + '\";'
            print(self.sql)
            self.cursor.execute(self.sql)
            self.data = self.cursor.fetchone()
            if self.data is None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '该房屋类型并不存在！')
            else:
                self.sql = 'select * from housetype where typeID = \"' + self.searchHouseTypeID.text() + '\";'
                self.cursor.execute(self.sql)
                self.houseTypeInfo = self.cursor.fetchall()
                self.dataToHouseTypeTable(self.houseTypeInfo)

    # def returnFun(self):
    #





if __name__ == "__main__":
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="exp3")
    cursor = db.cursor()
    ##每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    searchUI = searchUI(db, cursor)
    searchUI.show()
    sys.exit(app.exec_())

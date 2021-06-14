# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserManage.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
from PyQt5.QtSql import *
import time
import sip
import db


class UserManage(QDialog):

    def __init__(self, parent=None):
        super(UserManage, self).__init__(parent)
        self.resize(280, 400)

        self.setWindowTitle("管理用户")
        # 用户数
        self.userCount = 0
        self.oldDeleteId = ""
        self.oldDeleteName = ""
        self.deleteId = ""
        self.deleteName = ""
        self.setupUi()

    def setupUi(self):


        self.getResult()

        # UserManage.setObjectName("UserManage")
        # UserManage.resize(280, 418)
        self.formLayout = QtWidgets.QFormLayout(self)
        self.formLayout.setObjectName("formLayout")

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setRowCount(self.userCount)
        item = QtWidgets.QTableWidgetItem()
        item.setText("学号")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("姓名")
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tableWidget)

        # 不可编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 整行选中
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.setRows()

        self.widget = QtWidgets.QWidget(self)
        self.widget.setMinimumSize(QtCore.QSize(0, 48))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hlayout = QtWidgets.QHBoxLayout()
        self.hlayout.setObjectName("hlayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(180, 36))
        self.pushButton.setObjectName("pushButton")
        self.hlayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.hlayout)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.widget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # 设置信号
        self.pushButton.clicked.connect(self.deleteUser)
        self.tableWidget.itemClicked.connect(self.getStudentInfo)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("", "管理用户"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("", "姓名", ))
        self.pushButton.setText(_translate("", "删 除 用 户"))

    def getResult(self):
        sql = "SELECT StudentId,Name FROM User WHERE IsAdmin=0"
        self.query = db.query(sql)

        if self.query != ():
            self.userCount = len(self.query);
        # sql = "SELECT StudentId,Name FROM User WHERE IsAdmin=0"
        # self.query = db.query(sql)

    def setRows(self):
        font = QFont()
        font.setPixelSize(14)
        for i in range(self.userCount):
            StudentIdItem = QTableWidgetItem(self.query[i][0])
            StudentNameItem = QTableWidgetItem(self.query[i][1])
            StudentIdItem.setFont(font)
            StudentNameItem.setFont(font)
            # StudentIdItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            # StudentNameItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.tableWidget.setItem(i, 0, StudentIdItem)
            self.tableWidget.setItem(i, 1, StudentNameItem)
        return

    def getStudentInfo(self, item):
        row = self.tableWidget.currentIndex().row()
        self.tableWidget.verticalScrollBar().setSliderPosition(row)
        self.getResult()

        if (self.query != ()):
            i = row
        self.oldDeleteId = self.deleteId
        self.oldDeleteName = self.deleteName
        self.deleteId = self.query[i][0]
        self.deleteName = self.query[i][1]

    def deleteUser(self):
        if (self.deleteId == "" and self.deleteName == ""):
            print(QMessageBox.warning(self, "警告", "请选中要删除的用户", QMessageBox.Yes, QMessageBox.Yes))
            return

        if (QMessageBox.information(self, "提醒", "删除用户:%s,%s\n用户一经删除将无法恢复，是否继续?" % (self.deleteId, self.deleteName),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No) == QMessageBox.No):
            return
        # 从User表删除用户
        sql = "DELETE FROM User WHERE StudentId='%s'" % (self.deleteId)
        db.exec_(sql)
        # 归还所有书籍
        sql = "SELECT * FROM User_Book  WHERE StudentId='%s' AND BorrowState=1" % self.deleteId
        self.query = db.query(sql)
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        while (self.query != ()):
            bookId = self.query[0][1]
            sql = "UPDATE Book SET NumCanBorrow=NumCanBorrow+1 WHERE BookId='%s'" % bookId
            db.exec_(sql)

        sql = "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BorrowState=1" % (
            timenow, self.deleteId)
        db.exec_(sql)

        print(QMessageBox.information(self, "提醒", "删除用户成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.updateUI()
        return

    def updateUI(self):
        self.getResult()
        self.tableWidget.setRowCount(self.userCount)
        self.setRows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = UserManage()
    mainMindow.show()
    sys.exit(app.exec_())

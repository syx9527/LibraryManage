# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BorrowStatusViewer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle
import db


class BorrowStatusViewer(QWidget):
    def __init__(self, studentId):
        super(BorrowStatusViewer, self).__init__()

        self.studentId = studentId

        self.setupUi()

    def setupUi(self):

        # BorrowStatusViewer.setObjectName("BorrowStatusViewer", )
        self.resize(850, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.borrowedLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.borrowedLabel.setFont(font)
        self.borrowedLabel.setObjectName("borrowedLabel")
        self.verticalLayout.addWidget(self.borrowedLabel)

        self.borrowedTableView = QtWidgets.QTableWidget(self)
        self.borrowedTableView.setObjectName("borrowedTableView")

        # 不可编辑
        self.borrowedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.borrowedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.borrowedTableView.setColumnCount(7)

        self.borrowedQuery()
        self.borrowedTableView.setRowCount(self.borrowedRow)
        self.borrowedUI()


        item = QtWidgets.QTableWidgetItem()
        self.borrowedTableView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowedTableView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowedTableView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowedTableView.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowedTableView.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowedTableView.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowedTableView.setHorizontalHeaderItem(6, item)

        self.returnedLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.returnedLabel.setFont(font)
        self.returnedLabel.setObjectName("returnedLabel")

        self.returnedTableView = QtWidgets.QTableWidget(self)
        self.returnedTableView.setObjectName("returnedTableView")

        # 不可编辑
        self.returnedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.returnedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.returnedTableView.setColumnCount(8)

        self.returnedQuery()
        self.returnedTableView.setRowCount(self.returnedRow)
        self.returnedUI()


        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnedTableView.setHorizontalHeaderItem(7, item)

        self.returnedQuery()

        self.verticalLayout.addWidget(self.borrowedTableView)
        self.verticalLayout.addWidget(self.returnedLabel)
        self.verticalLayout.addWidget(self.returnedTableView)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("BorrowStatusViewer", "欢迎使用图书馆管理系统"))
        self.borrowedLabel.setText(_translate("BorrowStatusViewer", "未归还:"))
        # item = self.borrowedTableView.verticalHeaderItem(0)
        # item.setText(_translate("BorrowStatusViewer", "1"))

        # for row in range(10):
        #     item = self.tableWidget.verticalHeaderItem(row)
        #     item.setText(_translate("BookStorageViewer", str(row + 1)))

        item = self.borrowedTableView.horizontalHeaderItem(0)
        item.setText(_translate("BorrowStatusViewer", "书名"))
        item = self.borrowedTableView.horizontalHeaderItem(1)
        item.setText(_translate("BorrowStatusViewer", "书号"))
        item = self.borrowedTableView.horizontalHeaderItem(2)
        item.setText(_translate("BorrowStatusViewer", "作者"))
        item = self.borrowedTableView.horizontalHeaderItem(3)
        item.setText(_translate("BorrowStatusViewer", "分类"))
        item = self.borrowedTableView.horizontalHeaderItem(4)
        item.setText(_translate("BorrowStatusViewer", "出版社"))
        item = self.borrowedTableView.horizontalHeaderItem(5)
        item.setText(_translate("BorrowStatusViewer", "出版时间"))
        item = self.borrowedTableView.horizontalHeaderItem(6)
        item.setText(_translate("BorrowStatusViewer", "借出时间"))
        self.returnedLabel.setText(_translate("BorrowStatusViewer", "已归还:"))

        # item = self.returnedTableView.verticalHeaderItem(0)
        # item.setText(_translate("BorrowStatusViewer", "1"))

        item = self.returnedTableView.horizontalHeaderItem(0)
        item.setText(_translate("BorrowStatusViewer", "书名"))
        item = self.returnedTableView.horizontalHeaderItem(1)
        item.setText(_translate("BorrowStatusViewer", "书号"))
        item = self.returnedTableView.horizontalHeaderItem(2)
        item.setText(_translate("BorrowStatusViewer", "作者"))
        item = self.returnedTableView.horizontalHeaderItem(3)
        item.setText(_translate("BorrowStatusViewer", "分类"))
        item = self.returnedTableView.horizontalHeaderItem(4)
        item.setText(_translate("BorrowStatusViewer", "出版社"))
        item = self.returnedTableView.horizontalHeaderItem(5)
        item.setText(_translate("BorrowStatusViewer", "出版时间"))
        item = self.returnedTableView.horizontalHeaderItem(6)
        item.setText(_translate("BorrowStatusViewer", "借出时间"))
        item = self.returnedTableView.horizontalHeaderItem(7)
        item.setText(_translate("BorrowStatusViewer", "归还时间"))

    def borrowedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Auth,Category,Publisher,PublishTime,BorrowTime  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=1 AND StudentId='%s'" % self.studentId
        self.query = db.query(sql)
        self.borrowedRow = len(self.query)

        return

    def returnedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Auth,Category,Publisher,PublishTime,BorrowTime,ReturnTime  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=0 AND StudentId='%s'" % self.studentId
        self.query = db.query(sql)
        self.returnedRow = len(self.query)
        return

    def borrowedUI(self):

        for i in range(len(self.query)):
            for j in range(7):
                ite1 = QTableWidgetItem(str(self.query[i][j]))
                self.borrowedTableView.setItem(i, j, ite1)

        return

    def returnedUI(self):
        for i in range(len(self.query)):
            for j in range(8):
                ite1 = QTableWidgetItem(str(self.query[i][j]))
                self.returnedTableView.setItem(i, j, ite1)

        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = BorrowStatusViewer("PB15000135")
    mainMindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookStorageViewer.ui'
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


class BookStorageViewer(QWidget):

    def __init__(self):
        super(BookStorageViewer, self).__init__()

        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("欢迎使用图书馆管理系统")
        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecord = 0
        # 每页数据数
        self.pageRecord = 10

        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(1200, 500)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Hlayout1 = QtWidgets.QHBoxLayout()
        self.Hlayout1.setObjectName("Hlayout1")
        self.searchEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.searchEdit.setFont(font)
        self.searchEdit.setObjectName("searchEdit")
        self.Hlayout1.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.searchButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/search.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.searchButton.setIcon(icon)
        self.searchButton.setObjectName("searchButton")
        self.Hlayout1.addWidget(self.searchButton)
        self.condisionComboBox = QtWidgets.QComboBox(self)
        self.condisionComboBox.setMinimumSize(QtCore.QSize(0, 32))
        self.condisionComboBox.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.setObjectName("condisionComboBox")
        self.condisionComboBox.addItem("")
        self.condisionComboBox.addItem("")
        self.condisionComboBox.addItem("")
        self.condisionComboBox.addItem("")
        self.condisionComboBox.addItem("")
        self.Hlayout1.addWidget(self.condisionComboBox)
        self.verticalLayout_2.addLayout(self.Hlayout1)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        # 不可编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(self.pageRecord)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalWidget = QtWidgets.QWidget(self)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.horizontalWidget)
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setObjectName("widget")
        self.Hlayout = QtWidgets.QHBoxLayout(self.widget)
        self.Hlayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Hlayout.setObjectName("Hlayout")
        self.jumpToLabel = QtWidgets.QLabel(self.widget)
        self.jumpToLabel.setObjectName("jumpToLabel")
        self.Hlayout.addWidget(self.jumpToLabel)
        self.pageEdit = QtWidgets.QLineEdit(self.widget)
        self.pageEdit.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pageEdit.setObjectName("pageEdit")
        self.Hlayout.addWidget(self.pageEdit)
        self.pageLabel = QtWidgets.QLabel(self.widget)
        self.pageLabel.setObjectName("pageLabel")
        self.Hlayout.addWidget(self.pageLabel)
        self.jumpToButton = QtWidgets.QPushButton(self.widget)
        self.jumpToButton.setObjectName("jumpToButton")
        self.Hlayout.addWidget(self.jumpToButton)
        self.prevButton = QtWidgets.QPushButton(self.widget)
        self.prevButton.setObjectName("prevButton")
        self.Hlayout.addWidget(self.prevButton)
        self.backButton = QtWidgets.QPushButton(self.widget)
        self.backButton.setObjectName("backButton")
        self.Hlayout.addWidget(self.backButton)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.horizontalWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.searchButtonClicked()

        self.tableWidget.setRowCount(self.pageRecord)

        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.backButton.clicked.connect(self.backButtonClicked)
        self.jumpToButton.clicked.connect(self.jumpToButtonClicked)
        self.searchEdit.returnPressed.connect(self.searchButtonClicked)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("BookStorageViewer", "欢迎使用图书馆管理系统"))
        self.searchButton.setText(_translate("BookStorageViewer", "查询"))
        self.condisionComboBox.setItemText(0, _translate("BookStorageViewer", "按书名查询"))
        self.condisionComboBox.setItemText(1, _translate("BookStorageViewer", "按书号查询"))
        self.condisionComboBox.setItemText(2, _translate("BookStorageViewer", "按作者查询"))
        self.condisionComboBox.setItemText(3, _translate("BookStorageViewer", "按分类查询"))
        self.condisionComboBox.setItemText(4, _translate("BookStorageViewer", "按出版社查询"))

        for row in range(10):
            item = self.tableWidget.verticalHeaderItem(row)
            item.setText(_translate("BookStorageViewer", str(row + 1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BookStorageViewer", "书名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BookStorageViewer", "书号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BookStorageViewer", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BookStorageViewer", "分类"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("BookStorageViewer", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BookStorageViewer", "出版时间"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("BookStorageViewer", "库存"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("BookStorageViewer", "剩余可借"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("BookStorageViewer", "总借阅次数"))
        self.jumpToLabel.setText(_translate("BookStorageViewer", "跳转到第"))
        self.pageLabel.setText(_translate("BookStorageViewer", "/5页"))
        self.jumpToButton.setText(_translate("BookStorageViewer", "跳转"))
        self.prevButton.setText(_translate("BookStorageViewer", "前一页"))
        self.backButton.setText(_translate("BookStorageViewer", "后一页"))

    def setButtonStatus(self):
        if (self.currentPage == self.totalPage):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(False)
        if (self.currentPage == 1):
            self.backButton.setEnabled(True)
            self.prevButton.setEnabled(False)
        if (self.currentPage < self.totalPage and self.currentPage > 1):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(True)

    # 得到记录数
    def getTotalRecordCount(self):
        self.query = db.query("SELECT * FROM Book")

        self.totalRecord = len(self.query)
        return

    # 得到总页数
    def getPageCount(self):
        self.getTotalRecordCount()
        # 上取整
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        return

    # 分页记录查询
    def recordQuery(self, index):
        queryCondition = ""
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == "按书名查询"):
            conditionChoice = 'BookName'
        elif (conditionChoice == "按书号查询"):
            conditionChoice = 'BookId'
        elif (conditionChoice == "按作者查询"):
            conditionChoice = 'Auth'
        elif (conditionChoice == '按分类查询'):
            conditionChoice = 'Category'
        else:
            conditionChoice = 'Publisher'

        if (self.searchEdit.text() == ""):
            self.queryCondition = "select * from Book"
            self.query = db.query(self.queryCondition)
            self.totalRecord = len(self.query)
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            queryCondition = (
                    "select * from Book ORDER BY %s  limit %d,%d " % (conditionChoice, index, self.pageRecord))
            self.query = db.query(queryCondition)
            self.setButtonStatus()
            self.updateUI()
            return

        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%%"
        queryCondition = ("SELECT * FROM Book WHERE {} LIKE '{}' ORDER BY {} ".format(
            conditionChoice, s, conditionChoice))
        self.query = db.query(queryCondition)
        self.totalRecord = len(self.query)
        self.updateUI()

        # 当查询无记录时的操作
        if (self.totalRecord == 0):
            print(QMessageBox.information(self, "提醒", "查询无记录", QMessageBox.Yes, QMessageBox.Yes))
            queryCondition = "select * from Book"
            self.query = db.query(queryCondition)
            self.totalRecord = len(self.query)
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            queryCondition = (
                    "select * from Book ORDER BY %s  limit %d,%d " % (conditionChoice, index, self.pageRecord))
            self.query = db.query(queryCondition)
            self.setButtonStatus()
            self.updateUI()
            return

        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        label = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(label)
        queryCondition = ("SELECT * FROM Book WHERE %s LIKE '%s' ORDER BY %s LIMIT %d,%d " % (
            conditionChoice, s, conditionChoice, index, self.pageRecord))
        self.query = db.query(queryCondition)
        self.setButtonStatus()
        self.updateUI()
        return

    # 点击查询
    def searchButtonClicked(self):
        self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        self.getPageCount()
        s = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(s)
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向前翻页
    def prevButtonClicked(self):
        self.currentPage -= 1
        if (self.currentPage <= 1):
            self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向后翻页
    def backButtonClicked(self):
        self.currentPage += 1
        if (self.currentPage >= int(self.totalPage)):
            self.currentPage = int(self.totalPage)
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 点击跳转
    def jumpToButtonClicked(self):
        if (self.pageEdit.text().isdigit()):
            self.currentPage = int(self.pageEdit.text())
            if (self.currentPage > self.totalPage):
                self.currentPage = self.totalPage
            if (self.currentPage <= 1):
                self.currentPage = 1
        else:
            self.currentPage = 1
        index = (self.currentPage - 1) * self.pageRecord
        self.pageEdit.setText(str(self.currentPage))
        self.recordQuery(index)
        # print(self.pageRecord)
        # print(self.query)
        return

    def updateUI(self, *__args):
        for i in range(10):
            for j in range(9):
                if i < len(self.query):
                    ite1 = QTableWidgetItem(str(self.query[i][j]))
                else:
                    ite1 = QTableWidgetItem(None)
                self.tableWidget.setItem(i, j, ite1)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = BookStorageViewer()
    mainMindow.show()
    sys.exit(app.exec_())

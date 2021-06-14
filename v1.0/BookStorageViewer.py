#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:SYX
# createTime: 2021/5/6 15:44

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle
import db


class BookStorageViewer(QWidget):
    def __init__(self):
        super(BookStorageViewer, self).__init__()
        self.resize(1200, 500)
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
        self.setUpUI()

    def setUpUI(self):
        self.layout = QVBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

        # Hlayout1控件的初始化
        self.searchEdit = QLineEdit()
        self.searchEdit.setFixedHeight(32)
        font = QFont()
        font.setPixelSize(15)
        self.searchEdit.setFont(font)

        self.searchButton = QPushButton("查询")
        self.searchButton.setFixedHeight(32)
        self.searchButton.setFont(font)
        self.searchButton.setIcon(QIcon(QPixmap("./images/search.png")))

        self.condisionComboBox = QComboBox()
        searchCondision = ['按书名查询', '按书号查询', '按作者查询', '按分类查询', '按出版社查询']
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        self.Hlayout1.addWidget(self.searchEdit)
        self.Hlayout1.addWidget(self.searchButton)
        self.Hlayout1.addWidget(self.condisionComboBox)

        # Hlayout2初始化
        self.jumpToLabel = QLabel("跳转到第")
        self.pageEdit = QLineEdit()
        self.pageEdit.setFixedWidth(30)
        s = "/" + str(self.totalPage) + "页"
        self.pageLabel = QLabel(s)
        self.jumpToButton = QPushButton("跳转")
        self.prevButton = QPushButton("前一页")
        self.prevButton.setFixedWidth(60)
        self.backButton = QPushButton("后一页")
        self.backButton.setFixedWidth(60)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.jumpToLabel)
        Hlayout.addWidget(self.pageEdit)
        Hlayout.addWidget(self.pageLabel)
        Hlayout.addWidget(self.jumpToButton)
        Hlayout.addWidget(self.prevButton)
        Hlayout.addWidget(self.backButton)
        widget = QWidget()
        widget.setLayout(Hlayout)
        widget.setFixedWidth(300)
        self.Hlayout2.addWidget(widget)

        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.queryModel = QStandardItemModel()
        self.queryModel.setHorizontalHeaderLabels(["书名", "书号", "作者", "分类", "出版社", "出版时间", "库存", "剩余可借", "总借阅次数", ])
        self.searchButtonClicked()

        self.tableView.setModel(self.queryModel)

        # self.ite1 = QStandardItem(self.query[0][0])
        # self.queryModel.setItem(0,0,self.ite1)

        self.layout.addLayout(self.Hlayout1)
        self.layout.addWidget(self.tableView)
        self.layout.addLayout(self.Hlayout2)
        self.setLayout(self.layout)

        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.backButton.clicked.connect(self.backButtonClicked)
        self.jumpToButton.clicked.connect(self.jumpToButtonClicked)
        self.searchEdit.returnPressed.connect(self.searchButtonClicked)

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
                    ite1 = QStandardItem(str(self.query[i][j]))
                else:
                    ite1 = QStandardItem(None)
                self.queryModel.setItem(i, j, ite1)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = BookStorageViewer()
    mainMindow.show()
    sys.exit(app.exec_())

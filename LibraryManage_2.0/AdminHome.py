# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminHome.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle
from addBookDialog import addBookDialog
from dropBookDialog import dropBookDialog
from BookStorageViewer import BookStorageViewer

from UserManage import UserManage

class AdminHome(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AdminHome")
        self.resize(1200, 600)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("layout")
        self.buttonlayout = QtWidgets.QVBoxLayout()
        self.buttonlayout.setObjectName("buttonlayout")
        self.addBookButton = QtWidgets.QPushButton(self)
        self.addBookButton.setEnabled(True)
        self.addBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addBookButton.setFont(font)
        self.addBookButton.setObjectName("addBookButton")
        self.buttonlayout.addWidget(self.addBookButton)
        self.dropBookButton = QtWidgets.QPushButton(self)
        self.dropBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dropBookButton.setFont(font)
        self.dropBookButton.setObjectName("dropBookButton")
        self.buttonlayout.addWidget(self.dropBookButton)
        self.userManageButton = QtWidgets.QPushButton(self)
        self.userManageButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userManageButton.setFont(font)
        self.userManageButton.setObjectName("userManageButton")
        self.buttonlayout.addWidget(self.userManageButton)
        self.layout.addLayout(self.buttonlayout)
        self.storageView = BookStorageViewer()
        self.layout.addWidget(self.storageView)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AdminHome", "欢迎使用图书馆管理系统"))
        self.addBookButton.setText(_translate("AdminHome", "添加书籍"))
        self.dropBookButton.setText(_translate("AdminHome", "淘汰书籍"))
        self.userManageButton.setText(_translate("AdminHome", "用户管理"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = AdminHome()
    mainMindow.show()
    sys.exit(app.exec_())
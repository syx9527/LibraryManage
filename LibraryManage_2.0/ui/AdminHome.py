# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminHome.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminHome(object):
    def setupUi(self, AdminHome):
        AdminHome.setObjectName("AdminHome")
        AdminHome.resize(1200, 600)
        self.layout = QtWidgets.QHBoxLayout(AdminHome)
        self.layout.setObjectName("layout")
        self.buttonlayout = QtWidgets.QVBoxLayout()
        self.buttonlayout.setObjectName("buttonlayout")
        self.addBookButton = QtWidgets.QPushButton(AdminHome)
        self.addBookButton.setEnabled(True)
        self.addBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addBookButton.setFont(font)
        self.addBookButton.setObjectName("addBookButton")
        self.buttonlayout.addWidget(self.addBookButton)
        self.dropBookButton = QtWidgets.QPushButton(AdminHome)
        self.dropBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dropBookButton.setFont(font)
        self.dropBookButton.setObjectName("dropBookButton")
        self.buttonlayout.addWidget(self.dropBookButton)
        self.userManageButton = QtWidgets.QPushButton(AdminHome)
        self.userManageButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userManageButton.setFont(font)
        self.userManageButton.setObjectName("userManageButton")
        self.buttonlayout.addWidget(self.userManageButton)
        self.layout.addLayout(self.buttonlayout)

        self.retranslateUi(AdminHome)
        QtCore.QMetaObject.connectSlotsByName(AdminHome)

    def retranslateUi(self, AdminHome):
        _translate = QtCore.QCoreApplication.translate
        AdminHome.setWindowTitle(_translate("AdminHome", "欢迎使用图书馆管理系统"))
        self.addBookButton.setText(_translate("AdminHome", "添加书籍"))
        self.dropBookButton.setText(_translate("AdminHome", "淘汰书籍"))
        self.userManageButton.setText(_translate("AdminHome", "用户管理"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentHome.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentHome(object):
    def setupUi(self, StudentHome):
        StudentHome.setObjectName("StudentHome")
        StudentHome.resize(1200, 600)
        self.layout = QtWidgets.QHBoxLayout(StudentHome)
        self.layout.setObjectName("layout")
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.borrowBookButton = QtWidgets.QPushButton(StudentHome)
        self.borrowBookButton.setEnabled(True)
        self.borrowBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.borrowBookButton.setFont(font)
        self.borrowBookButton.setObjectName("borrowBookButton")
        self.buttonLayout.addWidget(self.borrowBookButton)
        self.returnBookButton = QtWidgets.QPushButton(StudentHome)
        self.returnBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setObjectName("returnBookButton")
        self.buttonLayout.addWidget(self.returnBookButton)
        self.myBookStatus = QtWidgets.QPushButton(StudentHome)
        self.myBookStatus.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.myBookStatus.setFont(font)
        self.myBookStatus.setObjectName("myBookStatus")
        self.buttonLayout.addWidget(self.myBookStatus)
        self.allBookButton = QtWidgets.QPushButton(StudentHome)
        self.allBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.allBookButton.setFont(font)
        self.allBookButton.setObjectName("allBookButton")
        self.buttonLayout.addWidget(self.allBookButton)
        self.layout.addLayout(self.buttonLayout)

        self.retranslateUi(StudentHome)
        QtCore.QMetaObject.connectSlotsByName(StudentHome)

    def retranslateUi(self, StudentHome):
        _translate = QtCore.QCoreApplication.translate
        StudentHome.setWindowTitle(_translate("StudentHome", "欢迎使用图书馆管理系统"))
        self.borrowBookButton.setText(_translate("StudentHome", "借书"))
        self.returnBookButton.setText(_translate("StudentHome", "还书"))
        self.myBookStatus.setText(_translate("StudentHome", "借阅状态"))
        self.allBookButton.setText(_translate("StudentHome", "所有书籍"))



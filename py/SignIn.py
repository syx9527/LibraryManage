# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignIn.ui'
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
import time

import db


class Ui_SignInWidget(object):
    def setupUi(self, SignInWidget):
        SignInWidget.setObjectName("SignInWidget")
        SignInWidget.resize(1200, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(SignInWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Hlayout1 = QtWidgets.QHBoxLayout()
        self.Hlayout1.setObjectName("Hlayout1")
        self.label = QtWidgets.QLabel(SignInWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 390))
        self.label.setMaximumSize(QtCore.QSize(16777215, 390))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Hlayout1.addWidget(self.label)
        self.verticalLayout.addLayout(self.Hlayout1)
        self.Hlayout2 = QtWidgets.QHBoxLayout()
        self.Hlayout2.setObjectName("Hlayout2")
        self.formlayout = QtWidgets.QFormLayout()
        self.formlayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formlayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formlayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formlayout.setHorizontalSpacing(0)
        self.formlayout.setVerticalSpacing(5)
        self.formlayout.setObjectName("formlayout")
        self.label1 = QtWidgets.QLabel(SignInWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.formlayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.lineEdit1 = QtWidgets.QLineEdit(SignInWidget)
        self.lineEdit1.setMaximumSize(QtCore.QSize(180, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setMaxLength(12)
        self.lineEdit1.setObjectName("lineEdit1")
        self.formlayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit1)
        self.label2 = QtWidgets.QLabel(SignInWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.formlayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.lineEdit2 = QtWidgets.QLineEdit(SignInWidget)
        self.lineEdit2.setMaximumSize(QtCore.QSize(180, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setMaxLength(16)
        self.lineEdit2.setObjectName("lineEdit2")
        self.formlayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit2)
        self.pushButton = QtWidgets.QPushButton(SignInWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formlayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.Hlayout2.addLayout(self.formlayout)
        self.verticalLayout.addLayout(self.Hlayout2)

        self.retranslateUi(SignInWidget)
        QtCore.QMetaObject.connectSlotsByName(SignInWidget)

    def retranslateUi(self, SignInWidget):
        _translate = QtCore.QCoreApplication.translate
        SignInWidget.setWindowTitle(_translate("SignInWidget", "欢迎使用图书馆管理系统"))
        self.label.setText(_translate("SignInWidget", "欢迎使用图书馆管理系统"))
        self.label1.setText(_translate("SignInWidget", "学号: "))
        self.label2.setText(_translate("SignInWidget", "密码: "))
        self.pushButton.setText(_translate("SignInWidget", "登 录"))



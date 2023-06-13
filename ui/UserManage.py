# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserManage.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserManage(object):
    def setupUi(self, UserManage):
        UserManage.setObjectName("UserManage")
        UserManage.resize(280, 418)
        self.formLayout = QtWidgets.QFormLayout(UserManage)
        self.formLayout.setObjectName("formLayout")
        self.tableWidget = QtWidgets.QTableWidget(UserManage)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("学号")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tableWidget)
        self.widget = QtWidgets.QWidget(UserManage)
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

        self.retranslateUi(UserManage)
        QtCore.QMetaObject.connectSlotsByName(UserManage)

    def retranslateUi(self, UserManage):
        _translate = QtCore.QCoreApplication.translate
        UserManage.setWindowTitle(_translate("UserManage", "管理用户"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("UserManage", "姓名"))
        self.pushButton.setText(_translate("UserManage", "删 除 用 户"))



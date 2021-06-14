# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.bar = QtWidgets.QMenuBar(MainWindow)
        self.bar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.bar.setObjectName("bar")
        self.menu = QtWidgets.QMenu(self.bar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.bar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.signUpAction = QtWidgets.QAction(MainWindow)
        self.signUpAction.setObjectName("signUpAction")
        self.changePasswordAction = QtWidgets.QAction(MainWindow)
        self.changePasswordAction.setObjectName("changePasswordAction")
        self.signInAction = QtWidgets.QAction(MainWindow)
        self.signInAction.setEnabled(False)
        self.signInAction.setObjectName("signInAction")
        self.quitSignInAction = QtWidgets.QAction(MainWindow)
        self.quitSignInAction.setEnabled(False)
        self.quitSignInAction.setObjectName("quitSignInAction")
        self.quitAction = QtWidgets.QAction(MainWindow)
        self.quitAction.setObjectName("quitAction")
        self.menu.addAction(self.signUpAction)
        self.menu.addAction(self.changePasswordAction)
        self.menu.addAction(self.signInAction)
        self.menu.addAction(self.quitSignInAction)
        self.menu.addAction(self.quitAction)
        self.bar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "菜单栏"))
        self.action.setText(_translate("MainWindow", "修改密码"))
        self.signUpAction.setText(_translate("MainWindow", "注册"))
        self.changePasswordAction.setText(_translate("MainWindow", "修改密码"))
        self.signInAction.setText(_translate("MainWindow", "登录"))
        self.quitSignInAction.setText(_translate("MainWindow", "退出登录"))
        self.quitAction.setText(_translate("MainWindow", "退出"))


import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import qdarkstyle
from SignIn import SignInWidget
from SignUp import SignUpWidget
import sip
from AdminHome import AdminHome
from StudentHome import StudentHome
from changePasswordDialog import changePasswordDialog


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.widget = SignInWidget()
        self.resize(1200, 600)

        self.setCentralWidget(self.widget)

        bar = self.menuBar()
        self.Menu = bar.addMenu("菜单栏")
        self.signUpAction = QAction("注册", self)
        self.changePasswordAction =QAction("修改密码",self)
        self.signInAction = QAction("登录", self)
        self.quitSignInAction = QAction("退出登录", self)
        self.quitAction = QAction("退出", self)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.changePasswordAction)
        self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "欢迎登陆图书馆管理系统"))
        self.Menu.setTitle(_translate("MainWindow", "菜单栏"))
        self.changePasswordAction.setText(_translate("MainWindow", "修改密码"))
        self.signUpAction.setText(_translate("MainWindow", "注册"))
        self.changePasswordAction.setText(_translate("MainWindow", "修改密码"))
        self.signInAction.setText(_translate("MainWindow", "登录"))
        self.quitSignInAction.setText(_translate("MainWindow", "退出登录"))
        self.quitAction.setText(_translate("MainWindow", "退出"))

    def adminSignIn(self):
        sip.delete(self.widget)
        self.widget = AdminHome()
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def studentSignIn(self, studentId):
        sip.delete(self.widget)
        self.widget = StudentHome(studentId)
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def menuTriggered(self, q):
        if (q.text() == "修改密码"):
            changePsdDialog = changePasswordDialog(self)
            changePsdDialog.show()
            changePsdDialog.exec_()
        if (q.text() == "注册"):
            sip.delete(self.widget)
            self.widget = SignUpWidget()
            self.setCentralWidget(self.widget)
            self.widget.student_signup_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(False)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(True)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出"):
            qApp = QApplication.instance()
            qApp.quit()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Main()
    mainMindow.show()
    sys.exit(app.exec_())

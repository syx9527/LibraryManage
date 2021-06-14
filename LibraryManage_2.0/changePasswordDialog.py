# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePasswordDialog.ui'
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
import hashlib
import db


class changePasswordDialog(QDialog):
    def __init__(self, parent=None):
        super(changePasswordDialog, self).__init__(parent)

        self.setupUi()

    def setupUi(self):
        # self.setObjectName("changePasswordDialog")
        self.resize(280, 300)
        self.formLayout = QtWidgets.QFormLayout(self)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.studentIdLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studentIdLabel.setFont(font)
        self.studentIdLabel.setObjectName("studentIdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.studentIdLabel)
        self.studentIdEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.studentIdEdit.setFont(font)
        self.studentIdEdit.setMaxLength(12)
        self.studentIdEdit.setObjectName("studentIdEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.studentIdEdit)
        self.oldPasswordLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.oldPasswordLabel.setFont(font)
        self.oldPasswordLabel.setObjectName("oldPasswordLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.oldPasswordLabel)
        self.passwordLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.confirmPasswordLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.confirmPasswordLabel.setFont(font)
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.confirmPasswordLabel)
        self.oldPasswordEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oldPasswordEdit.setFont(font)
        self.oldPasswordEdit.setMaxLength(16)
        self.oldPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPasswordEdit.setObjectName("oldPasswordEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.oldPasswordEdit)
        self.passwordEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setMaxLength(16)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.passwordEdit)
        self.confirmPasswordEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmPasswordEdit.setFont(font)
        self.confirmPasswordEdit.setMaxLength(16)
        self.confirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPasswordEdit.setObjectName("confirmPasswordEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.confirmPasswordEdit)
        self.titlelabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titlelabel.setFont(font)
        self.titlelabel.setObjectName("titlelabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titlelabel)
        self.changePasswordButton = QtWidgets.QPushButton(self)
        self.changePasswordButton.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.changePasswordButton.setFont(font)
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.changePasswordButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.changePasswordButton.clicked.connect(self.changePasswordButtonClicked)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("changePasswordDialog", "修改密码"))
        self.studentIdLabel.setText(_translate("changePasswordDialog", "学    号："))
        self.oldPasswordLabel.setText(_translate("changePasswordDialog", "旧 密 码："))
        self.passwordLabel.setText(_translate("changePasswordDialog", "新 密 码："))
        self.confirmPasswordLabel.setText(_translate("changePasswordDialog", "确认密码："))
        self.titlelabel.setText(_translate("changePasswordDialog", "修改密码"))
        self.changePasswordButton.setText(_translate("changePasswordDialog", "确认修改"))

    def changePasswordButtonClicked(self):
        studentId = self.studentIdEdit.text()
        oldPassword = self.oldPasswordEdit.text()
        password = self.passwordEdit.text()
        confirmPassword = self.confirmPasswordEdit.text()
        if (studentId == "" or oldPassword == "" or password == "" or confirmPassword == ""):
            print(QMessageBox.warning(self, "警告", "输入不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            return

        sql = "SELECT * FROM User WHERE StudentId='%s'" % studentId
        query = db.query(sql)
        # 如果用户不存在
        if (query == ()):
            print(QMessageBox.warning(self, "警告", "该用户不存在，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            self.studentIdEdit.clear()
            return
            # 如果密码错误
        hl = hashlib.md5()
        hl.update(oldPassword.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        sql = "SELECT * FROM User WHERE Password='%s' AND StudentId='%s'" % (md5password, studentId)
        query = db.query(sql)
        if (query == ()):
            print(QMessageBox.warning(self, "警告", "原密码输入错误,请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            self.oldPasswordEdit.clear()
            return
        # 密码与确认密码不同
        if (password != confirmPassword):
            print(QMessageBox.warning(self, "警告", "两次输入密码不同,请确认输入", QMessageBox.Yes, QMessageBox.Yes))
            self.passwordEdit.clear()
            self.confirmPasswordEdit.clear()
            return
        # 修改密码
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        sql = "UPDATE User SET Password='%s' WHERE StudentId='%s'" % (md5password, studentId)
        db.exec_(sql)

        QMessageBox.information(self, "提醒", "修改密码成功，请登录系统!", QMessageBox.Yes, QMessageBox.Yes)
        self.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = changePasswordDialog()
    mainMindow.show()
    sys.exit(app.exec_())

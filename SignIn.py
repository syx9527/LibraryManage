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
import hashlib
import db


class SignInWidget(QtWidgets.QWidget):
    is_admin_signal = pyqtSignal()
    is_student_signal = pyqtSignal(str)

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.setupUi()

    def setupUi(self, ):
        # self.setObjectName("SignInWidget")
        self.resize(1200, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Hlayout1 = QtWidgets.QHBoxLayout()
        self.Hlayout1.setObjectName("Hlayout1")
        self.label = QtWidgets.QLabel(self)

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
        self.formlayout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formlayout.setHorizontalSpacing(0)
        self.formlayout.setVerticalSpacing(5)
        self.formlayout.setObjectName("formlayout")
        self.label1 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.formlayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setMaximumSize(QtCore.QSize(180, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setMaxLength(12)
        self.lineEdit1.setObjectName("lineEdit1")
        self.formlayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit1)
        self.label2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.formlayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setMaximumSize(QtCore.QSize(180, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setMaxLength(16)
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit2.setObjectName("lineEdit2")
        self.formlayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit2)
        self.signIn = QtWidgets.QPushButton(self)
        self.signIn.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signIn.setFont(font)
        self.signIn.setObjectName("signIn")
        self.formlayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.signIn)
        self.Hlayout2.addLayout(self.formlayout)
        self.verticalLayout.addLayout(self.Hlayout2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.signIn.clicked.connect(self.signInCheck)
        self.lineEdit2.returnPressed.connect(self.signInCheck)
        self.lineEdit1.returnPressed.connect(self.signInCheck)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SignInWidget", "欢迎使用图书馆管理系统"))
        self.label.setText(_translate("SignInWidget", "欢迎使用图书馆管理系统"))
        self.label1.setText(_translate("SignInWidget", "学号: "))
        self.label2.setText(_translate("SignInWidget", "密码: "))
        self.signIn.setText(_translate("SignInWidget", "登 录"))

    def signInCheck(self):
        studentId = self.lineEdit1.text()
        password = self.lineEdit2.text()
        if (studentId == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "学号和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return

        sql = "SELECT * FROM user WHERE StudentId='%s'" % (studentId)

        query = db.query(sql)

        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))

        if (query == ()):
            print(QMessageBox.information(self, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
        else:
            query = query[0]
            if (studentId == query[0] and hl.hexdigest() == query[2]):
                # 如果是管理员
                if (query[3] == 1):
                    self.is_admin_signal.emit()
                else:
                    self.is_student_signal.emit(studentId)
            else:
                print(QMessageBox.information(self, "提示", "密码错误!", QMessageBox.Yes, QMessageBox.Yes))
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = SignInWidget()
    mainMindow.show()
    sys.exit(app.exec_())


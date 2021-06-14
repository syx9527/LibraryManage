# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp.ui'
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


class SignUpWidget(QtWidgets.QWidget):
    student_signup_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self, ):
        self.setObjectName("SignUpWidget")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setEnabled(True)
        self.resize(1200, 600)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setMaximumSize(QtCore.QSize(1201, 600))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setStyleSheet("")
        self.formLayout_4 = QtWidgets.QFormLayout(self)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setSpacing(0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, 0, 50)
        self.verticalLayout.setSpacing(160)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signUpLabel = QtWidgets.QLabel(self)
        self.signUpLabel.setMinimumSize(QtCore.QSize(180, 32))
        self.signUpLabel.setMaximumSize(QtCore.QSize(1200, 600))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.signUpLabel.setFont(font)
        self.signUpLabel.setLineWidth(1)
        self.signUpLabel.setTextFormat(QtCore.Qt.AutoText)
        self.signUpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signUpLabel.setObjectName("signUpLabel")
        self.verticalLayout.addWidget(self.signUpLabel)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.studentIdLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studentIdLabel.setFont(font)
        self.studentIdLabel.setObjectName("studentIdLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.studentIdLabel)
        self.studentIdLineEdit = QtWidgets.QLineEdit(self)
        self.studentIdLineEdit.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studentIdLineEdit.setFont(font)
        self.studentIdLineEdit.setInputMask("")
        self.studentIdLineEdit.setText("")
        self.studentIdLineEdit.setMaxLength(12)
        self.studentIdLineEdit.setDragEnabled(False)
        self.studentIdLineEdit.setPlaceholderText("")
        self.studentIdLineEdit.setObjectName("studentIdLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.studentIdLineEdit)
        self.studentNameLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studentNameLabel.setFont(font)
        self.studentNameLabel.setObjectName("studentNameLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.studentNameLabel)
        self.studentNameLineEdit = QtWidgets.QLineEdit(self)
        self.studentNameLineEdit.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studentNameLineEdit.setFont(font)
        self.studentNameLineEdit.setMaxLength(10)
        self.studentNameLineEdit.setObjectName("studentNameLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.studentNameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self)
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setMaxLength(16)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.passwordConfirmLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordConfirmLabel.setFont(font)
        self.passwordConfirmLabel.setObjectName("passwordConfirmLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.passwordConfirmLabel)
        self.passwordConfirmLineEdit = QtWidgets.QLineEdit(self)
        self.passwordConfirmLineEdit.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordConfirmLineEdit.setFont(font)
        self.passwordConfirmLineEdit.setMaxLength(16)
        self.passwordConfirmLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordConfirmLineEdit.setObjectName("passwordConfirmLineEdit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passwordConfirmLineEdit)
        self.signUpbutton = QtWidgets.QPushButton(self)
        self.signUpbutton.setMinimumSize(QtCore.QSize(120, 30))
        self.signUpbutton.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signUpbutton.setFont(font)
        self.signUpbutton.setObjectName("signUpbutton")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.signUpbutton)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.signUpbutton.clicked.connect(self.SignUp)
        self.studentIdLineEdit.returnPressed.connect(self.SignUp)
        self.studentNameLineEdit.returnPressed.connect(self.SignUp)
        self.passwordLineEdit.returnPressed.connect(self.SignUp)
        self.passwordConfirmLineEdit.returnPressed.connect(self.SignUp)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SignUpWidget", "欢迎登陆图书馆管理系统"))
        self.signUpLabel.setText(_translate("SignUpWidget",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">注 册</span></p></body></html>"))
        self.studentIdLabel.setText(_translate("SignUpWidget", "学  号:"))
        self.studentNameLabel.setText(_translate("SignUpWidget", "姓  名: "))
        self.passwordLabel.setText(_translate("SignUpWidget", "密  码: "))
        self.passwordConfirmLabel.setText(_translate("SignUpWidget", "确认密码: "))
        self.signUpbutton.setText(_translate("SignUpWidget", "注 册"))

    def SignUp(self):
        studentId = self.studentIdLineEdit.text()
        studentName = self.studentNameLineEdit.text()
        password = self.passwordLineEdit.text()
        confirmPassword = self.passwordConfirmLineEdit.text()
        if (studentId == "" or studentName == "" or password == "" or confirmPassword == ""):
            print(QMessageBox.warning(self, "警告", "表单不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:  # 需要处理逻辑，1.账号已存在;2.密码不匹配;3.插入user表

            if (confirmPassword != password):
                print(QMessageBox.warning(self, "警告", "两次输入密码不一致，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
                return
            elif (confirmPassword == password):
                # md5编码
                hl = hashlib.md5()
                hl.update(password.encode(encoding='utf-8'))
                md5password = hl.hexdigest()

                sql = "SELECT * FROM user WHERE StudentId='%s'" % (studentId)
                query = db.query(sql)

                if (not query == ()):
                    print(QMessageBox.warning(self, "警告", "该账号已存在,请重新输入", QMessageBox.Yes, QMessageBox.Yes))
                    return
                else:
                    sql = "INSERT INTO user VALUES ('%s','%s','%s',0,0,0)" % (
                        studentId, studentName, md5password)
                    db.exec_(sql)

                    print(QMessageBox.information(self, "提醒", "您已成功注册账号!", QMessageBox.Yes, QMessageBox.Yes))
                    self.student_signup_signal.emit(studentId)
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = SignUpWidget()
    mainMindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returnBookDialog.ui'
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


class returnBookDialog(QDialog):
    return_book_success_signal = pyqtSignal()

    def __init__(self, StudentId, parent=None):
        super(returnBookDialog, self).__init__(parent)
        self.StudentId = StudentId
        self.setupUi()

    def setupUi(self):

        # self.setObjectName("returnBookDialog")
        self.resize(300, 400)
        self.formLayout = QtWidgets.QFormLayout(self)
        self.formLayout.setObjectName("formLayout")
        self.titlelabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titlelabel.setFont(font)
        self.titlelabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titlelabel.setLineWidth(1)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setObjectName("titlelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titlelabel)
        self.returnStudentLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.returnStudentLabel.setFont(font)
        self.returnStudentLabel.setObjectName("returnStudentLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.returnStudentLabel)

        self.returnStudentIdLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.returnStudentIdLabel.setFont(font)
        self.returnStudentIdLabel.setObjectName("returnStudentIdLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.returnStudentIdLabel)

        self.bookNameLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameLabel.setFont(font)
        self.bookNameLabel.setObjectName("bookNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookNameLabel)
        self.bookNameEdit = QtWidgets.QLineEdit(self)
        self.bookNameEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameEdit.setFont(font)
        self.bookNameEdit.setStyleSheet("#363636")
        self.bookNameEdit.setMaxLength(10)
        self.bookNameEdit.setObjectName("bookNameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookNameEdit)
        self.bookIdLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookIdLabel.setFont(font)
        self.bookIdLabel.setObjectName("bookIdLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.bookIdLabel)
        self.bookIdEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookIdEdit.setFont(font)
        self.bookIdEdit.setMaxLength(6)
        self.bookIdEdit.setObjectName("bookIdEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bookIdEdit)
        self.authNameLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authNameLabel.setFont(font)
        self.authNameLabel.setObjectName("authNameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.authNameLabel)
        self.authNameEdit = QtWidgets.QLineEdit(self)
        self.authNameEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authNameEdit.setFont(font)
        self.authNameEdit.setStyleSheet("#363636")
        self.authNameEdit.setMaxLength(10)
        self.authNameEdit.setObjectName("authNameEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.authNameEdit)
        self.categoryLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("categoryLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryComboBox = QtWidgets.QComboBox(self)
        self.categoryComboBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setStyleSheet("#363636")
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
        self.publisherLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherLabel.setFont(font)
        self.publisherLabel.setObjectName("publisherLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
        self.publisherEdit = QtWidgets.QLineEdit(self)
        self.publisherEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherEdit.setFont(font)
        self.publisherEdit.setStyleSheet("#363636")
        self.publisherEdit.setMaxLength(10)
        self.publisherEdit.setObjectName("publisherEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publisherEdit)
        self.publishDateLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publishDateLabel.setFont(font)
        self.publishDateLabel.setObjectName("publishDateLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.publishDateLabel)
        self.publishTime = QtWidgets.QDateEdit(self)
        self.publishTime.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publishTime.setFont(font)
        self.publishTime.setStyleSheet("#363636")
        self.publishTime.setObjectName("publishTime")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.publishTime)
        self.returnBookButton = QtWidgets.QPushButton(self)
        self.returnBookButton.setMaximumSize(QtCore.QSize(140, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setObjectName("returnBookButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.returnBookButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.returnBookButton.clicked.connect(self.returnButtonClicked)
        self.bookIdEdit.textChanged.connect(self.bookIdEditChanged)

    def retranslateUi(self):

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("returnBookDialog", "????????????"))
        self.titlelabel.setText(_translate("returnBookDialog", "????????????"))
        self.returnStudentLabel.setText(_translate("returnBookDialog", "??? ??? ???:"))
        self.returnStudentIdLabel.setText(_translate("returnBookDialog", self.StudentId))

        self.bookNameLabel.setText(_translate("returnBookDialog", "???    ???:"))
        self.bookIdLabel.setText(_translate("returnBookDialog", "???    ???:"))
        self.authNameLabel.setText(_translate("returnBookDialog", "???    ???:"))
        self.categoryLabel.setText(_translate("returnBookDialog", "???    ???:"))
        self.categoryComboBox.setItemText(0, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(1, _translate("returnBookDialog", "????????????"))
        self.categoryComboBox.setItemText(2, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(3, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(4, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(5, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(6, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(7, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(8, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(9, _translate("returnBookDialog", "????????????"))
        self.categoryComboBox.setItemText(10, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(11, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(12, _translate("returnBookDialog", "??????"))
        self.categoryComboBox.setItemText(13, _translate("returnBookDialog", "?????????"))
        self.categoryComboBox.setItemText(14, _translate("returnBookDialog", "?????????"))
        self.categoryComboBox.setItemText(15, _translate("returnBookDialog", "????????????"))
        self.categoryComboBox.setItemText(16, _translate("returnBookDialog", "??????"))
        self.publisherLabel.setText(_translate("returnBookDialog", "??? ??? ???:"))
        self.publishDateLabel.setText(_translate("returnBookDialog", "????????????:"))
        self.returnBookButton.setText(_translate("returnBookDialog", "????????????"))

    def returnButtonClicked(self):
        # ????????????????????????????????????????????????????????????
        # ??????Book_User???User?????????Book???
        BookId = self.bookIdEdit.text()
        # BookId???????????????
        if (BookId == ""):
            print(QMessageBox.warning(self, "??????", "?????????????????????????????????????????????", QMessageBox.Yes, QMessageBox.Yes))
            return
        # ???????????????
        # ???????????????
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.StudentId, BookId)
        query = db.query(sql)
        if (query == ()):
            print(QMessageBox.information(self, "??????", "???????????????????????????????????????", QMessageBox.Yes, QMessageBox.Yes))
            return
        # ??????User???
        sql = "UPDATE User SET NumBorrowed=NumBorrowed-1 WHERE StudentId='%s'" % self.StudentId
        db.exec_(sql)

        # ??????Book???
        sql = "UPDATE Book SET NumCanBorrow=NumCanBorrow+1 WHERE BookId='%s'" % BookId
        db.exec_(sql)

        # ??????User_Book???
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            timenow, self.StudentId, BookId)
        db.exec_(sql)

        print(QMessageBox.information(self, "??????", "????????????!", QMessageBox.Yes, QMessageBox.Yes))
        self.return_book_success_signal.emit()
        self.close()
        return

    def bookIdEditChanged(self):
        bookId = self.bookIdEdit.text()
        if (bookId == "" or len(bookId) < 6):
            self.bookNameEdit.clear()
            self.publisherEdit.clear()
            self.authNameEdit.clear()
            self.publishTime.clear()

        # ???User_Book??????????????????????????????????????????????????????form??????
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.StudentId, bookId)
        query = db.query(sql)
        if (query != ()):
            # ??????form??????
            sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
            query = db.query(sql)
            # ??????????????????????????????????????????form
            if (query != ()):
                query = query[0]
                self.bookNameEdit.setText(query[0])
                self.authNameEdit.setText(query[2])
                self.categoryComboBox.setCurrentText(query[3])
                self.publisherEdit.setText(query[4])
                self.publishTime.setDate(query[5])
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = returnBookDialog("PB15000135")
    mainMindow.show()
    sys.exit(app.exec_())

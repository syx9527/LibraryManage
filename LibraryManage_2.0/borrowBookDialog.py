# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrowBookDialog.ui'
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


class borrowBookDialog(QDialog):
    borrow_book_success_signal = pyqtSignal()

    def __init__(self, StudentId, parent=None):
        super(borrowBookDialog, self).__init__(parent)
        self.studentId = StudentId
        self.setupUi()


    def setupUi(self):

        # self.setObjectName("borrowBookDialog")
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

        self.borrowStudentLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.borrowStudentLabel.setFont(font)
        self.borrowStudentLabel.setObjectName("borrowStudentLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.borrowStudentLabel)
        self.bookNameLabel = QtWidgets.QLabel(self)

        self.borrowStudentIdLabel = QtWidgets.QLabel(self)
        self.borrowStudentIdLabel.setFont(font)
        self.borrowStudentIdLabel.setObjectName("borrowStudentIdLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.borrowStudentIdLabel)
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
        self.publishTime.setObjectName("publishTime")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.publishTime)
        self.borrowBookButton = QtWidgets.QPushButton(self)
        self.borrowBookButton.setMaximumSize(QtCore.QSize(140, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.borrowBookButton.setFont(font)
        self.borrowBookButton.setObjectName("borrowBookButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.borrowBookButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.borrowBookButton.clicked.connect(self.borrowButtonClicked)
        self.bookIdEdit.textChanged.connect(self.bookIdEditChanged)
        self.bookIdEdit.returnPressed.connect(self.borrowButtonClicked)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("borrowBookDialog", "????????????"))
        self.titlelabel.setText(_translate("borrowBookDialog", "????????????"))
        self.borrowStudentLabel.setText(_translate("borrowBookDialog", "??? ??? ???:"))
        self.borrowStudentIdLabel.setText(_translate("borrowBookDialog", self.studentId))

        self.bookNameLabel.setText(_translate("borrowBookDialog", "???    ???:"))
        self.bookIdLabel.setText(_translate("borrowBookDialog", "???    ???:"))
        self.authNameLabel.setText(_translate("borrowBookDialog", "???    ???:"))
        self.categoryLabel.setText(_translate("borrowBookDialog", "???    ???:"))
        self.categoryComboBox.setItemText(0, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(1, _translate("borrowBookDialog", "????????????"))
        self.categoryComboBox.setItemText(2, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(3, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(4, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(5, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(6, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(7, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(8, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(9, _translate("borrowBookDialog", "????????????"))
        self.categoryComboBox.setItemText(10, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(11, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(12, _translate("borrowBookDialog", "??????"))
        self.categoryComboBox.setItemText(13, _translate("borrowBookDialog", "?????????"))
        self.categoryComboBox.setItemText(14, _translate("borrowBookDialog", "?????????"))
        self.categoryComboBox.setItemText(15, _translate("borrowBookDialog", "????????????"))
        self.categoryComboBox.setItemText(16, _translate("borrowBookDialog", "??????"))
        self.publisherLabel.setText(_translate("borrowBookDialog", "??? ??? ???:"))
        self.publishDateLabel.setText(_translate("borrowBookDialog", "????????????:"))
        self.borrowBookButton.setText(_translate("borrowBookDialog", "????????????"))

    def borrowButtonClicked(self):
        # ???????????????????????????????????????????????????????????????
        # ???Book_User????????????????????????User?????????Book???
        BookId = self.bookIdEdit.text()
        # BookId???????????????
        if (BookId == ""):
            print(QMessageBox.warning(self, "??????", "?????????????????????????????????????????????", QMessageBox.Yes, QMessageBox.Yes))
            return

        # ??????BookId?????????
        sql = "SELECT * FROM Book WHERE BookId='%s'" % BookId
        query = db.query(sql)
        if (query == ()):
            print(QMessageBox.warning(self, "??????", "?????????????????????????????????????????????", QMessageBox.Yes, QMessageBox.Yes))
            return

        # ????????????5???
        sql = "SELECT COUNT(StudentId) FROM User_Book WHERE StudentId='%s' AND BorrowState=1" % (
            self.studentId)
        query = db.query(sql)
        if (query != ()):
            borrowNum = query[0][0]
            if (borrowNum == 5):
                QMessageBox.warning(self, "??????", "??????????????????????????????5??????,???????????????", QMessageBox.Yes, QMessageBox.Yes)
                return
        # ?????????????????????
        sql = "SELECT COUNT(StudentId) FROM User_Book WHERE  StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.studentId, BookId)
        query = db.query(sql)
        if (query != 0 and query[0][0]):
            QMessageBox.warning(self, "??????", "?????????????????????????????????????????????????????????", QMessageBox.Yes, QMessageBox.Yes)
            return
        # ??????User???
        sql = "UPDATE User SET TimesBorrowed=TimesBorrowed+1,NumBorrowed=NumBorrowed+1 WHERE StudentId='%s'" % self.studentId
        db.exec_(sql)
        # ??????Book???
        sql = "UPDATE Book SET NumCanBorrow=NumCanBorrow-1,NumBorrowed=NumBorrowed+1 WHERE BookId='%s'" % BookId
        db.exec_(sql)
        # ??????User_Book???
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "INSERT INTO User_Book VALUES ('%s','%s','%s',NULL,1)" % (self.studentId, BookId, timenow)
        db.exec_(sql)

        print(QMessageBox.information(self, "??????", "????????????!", QMessageBox.Yes, QMessageBox.Yes))
        self.borrow_book_success_signal.emit()
        self.close()
        return

    def bookIdEditChanged(self):
        bookId = self.bookIdEdit.text()
        if (bookId == ""):
            self.bookNameEdit.clear()
            self.publisherEdit.clear()
            self.authNameEdit.clear()
            self.publishTime.clear()

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
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = borrowBookDialog("PB15000135")
    mainMindow.show()
    sys.exit(app.exec_())

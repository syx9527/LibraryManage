# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addBookDialog.ui'
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


class addBookDialog(QDialog):
    add_book_success_signal = pyqtSignal()


    def __init__(self,parent=None):
        super().__init__(parent)
        # self.setObjectName("addBookDialog")
        self.resize(300, 400)
        self.formLayout = QtWidgets.QFormLayout(self)
        self.setupUi()

    def setupUi(self, ):

        self.titlelabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titlelabel.setFont(font)
        self.titlelabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titlelabel.setLineWidth(1)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setObjectName("titlelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titlelabel)
        self.bookNameLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameLabel.setFont(font)
        self.bookNameLabel.setObjectName("bookNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bookNameLabel)
        self.bookNameEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameEdit.setFont(font)
        self.bookNameEdit.setMaxLength(10)
        self.bookNameEdit.setObjectName("bookNameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bookNameEdit)
        self.bookIdLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookIdLabel.setFont(font)
        self.bookIdLabel.setObjectName("bookIdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookIdLabel)
        self.bookIdEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookIdEdit.setFont(font)
        self.bookIdEdit.setMaxLength(6)
        self.bookIdEdit.setObjectName("bookIdEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookIdEdit)
        self.authNameLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authNameLabel.setFont(font)
        self.authNameLabel.setObjectName("authNameLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.authNameLabel)
        self.authNameEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authNameEdit.setFont(font)
        self.authNameEdit.setMaxLength(10)
        self.authNameEdit.setObjectName("authNameEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.authNameEdit)
        self.categoryLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("categoryLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryComboBox = QtWidgets.QComboBox(self)
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
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
        self.publisherLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherLabel.setFont(font)
        self.publisherLabel.setObjectName("publisherLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
        self.publisherEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherEdit.setFont(font)
        self.publisherEdit.setMaxLength(10)
        self.publisherEdit.setObjectName("publisherEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.publisherEdit)
        self.publishDateLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publishDateLabel.setFont(font)
        self.publishDateLabel.setObjectName("publishDateLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.publishDateLabel)
        self.publishTime = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publishTime.setFont(font)
        self.publishTime.setObjectName("publishTime")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publishTime)
        self.addNumLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addNumLabel.setFont(font)
        self.addNumLabel.setObjectName("addNumLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.addNumLabel)
        self.addNumEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addNumEdit.setFont(font)
        self.addNumEdit.setMaxLength(12)
        self.addNumEdit.setObjectName("addNumEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.addNumEdit)
        self.addBookButton = QtWidgets.QPushButton(self)
        self.addBookButton.setMaximumSize(QtCore.QSize(140, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addBookButton.setFont(font)
        self.addBookButton.setObjectName("addBookButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.addBookButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.addBookButton.clicked.connect(self.addBookButtonCicked)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("addBookDialog", "????????????"))
        self.titlelabel.setText(_translate("addBookDialog", "  ????????????"))
        self.bookNameLabel.setText(_translate("addBookDialog", "???    ???:"))
        self.bookIdLabel.setText(_translate("addBookDialog", "???    ???:"))
        self.authNameLabel.setText(_translate("addBookDialog", "???    ???:"))
        self.categoryLabel.setText(_translate("addBookDialog", "???    ???:"))
        self.categoryComboBox.setItemText(0, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(1, _translate("addBookDialog", "????????????"))
        self.categoryComboBox.setItemText(2, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(3, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(4, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(5, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(6, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(7, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(8, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(9, _translate("addBookDialog", "????????????"))
        self.categoryComboBox.setItemText(10, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(11, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(12, _translate("addBookDialog", "??????"))
        self.categoryComboBox.setItemText(13, _translate("addBookDialog", "?????????"))
        self.categoryComboBox.setItemText(14, _translate("addBookDialog", "?????????"))
        self.categoryComboBox.setItemText(15, _translate("addBookDialog", "????????????"))
        self.categoryComboBox.setItemText(16, _translate("addBookDialog", "??????"))
        self.publisherLabel.setText(_translate("addBookDialog", "??? ??? ???:"))
        self.publishDateLabel.setText(_translate("addBookDialog", "????????????:"))
        self.addNumLabel.setText(_translate("addBookDialog", "???    ???:"))
        self.addBookButton.setText(_translate("addBookDialog", "??? ???"))

    def addBookButtonCicked(self):
        bookName = self.bookNameEdit.text()
        bookId = self.bookIdEdit.text()
        authName = self.authNameEdit.text()
        bookCategory = self.categoryComboBox.currentText()
        publisher = self.publisherEdit.text()
        publishTime = self.publishTime.text()
        addBookNum = self.addNumEdit.text()
        if (
                bookName == "" or bookId == "" or authName == "" or bookCategory == "" or publisher == "" or publishTime == "" or addBookNum == ""):
            print(QMessageBox.warning(self, "??????", "??????????????????????????????", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            addBookNum = int(addBookNum)

            # ?????????????????????update Book???????????????????????????????????????????????????insert Book????????????insert buyordrop???
            sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
            query = db.query(sql)

            if (not query == ()):
                sql = "UPDATE Book SET NumStorage=NumStorage+%d,NumCanBorrow=NumCanBorrow+%d WHERE BookId='%s'" % (
                    addBookNum, addBookNum, bookId)
            else:
                sql = "INSERT INTO book VALUES ('%s','%s','%s','%s','%s','%s',%d,%d,0)" % (
                    bookName, bookId, authName, bookCategory, publisher, publishTime, addBookNum, addBookNum)
            db.exec_(sql)
            # ??????droporinsert???
            timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            sql = "INSERT INTO buyordrop VALUES ('%s','%s',1,%d)" % (bookId, timenow, addBookNum)
            db.exec_(sql)

            print(QMessageBox.information(self, "??????", "??????????????????!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_book_success_signal.emit()
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.bookNameEdit.clear()
        self.bookIdEdit.clear()
        self.authNameEdit.clear()
        self.addNumEdit.clear()
        self.publisherEdit.clear()


if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # Form = QtWidgets.QDialog()
    # ui = addBookDialog()
    # ui.setupUi(Form)
    # Form.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = addBookDialog()
    mainMindow.show()
    sys.exit(app.exec_())


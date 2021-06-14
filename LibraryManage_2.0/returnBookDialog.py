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
        self.studentId = StudentId
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
        self.studentId
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("returnBookDialog", "归还书籍"))
        self.titlelabel.setText(_translate("returnBookDialog", "归还书籍"))
        self.returnStudentLabel.setText(_translate("returnBookDialog", "还 书 人:"))
        self.returnStudentIdLabel.setText(_translate("returnBookDialog", self.studentId))

        self.bookNameLabel.setText(_translate("returnBookDialog", "书    名:"))
        self.bookIdLabel.setText(_translate("returnBookDialog", "书    号:"))
        self.authNameLabel.setText(_translate("returnBookDialog", "作    者:"))
        self.categoryLabel.setText(_translate("returnBookDialog", "分    类:"))
        self.categoryComboBox.setItemText(0, _translate("returnBookDialog", "哲学"))
        self.categoryComboBox.setItemText(1, _translate("returnBookDialog", "社会科学"))
        self.categoryComboBox.setItemText(2, _translate("returnBookDialog", "政治"))
        self.categoryComboBox.setItemText(3, _translate("returnBookDialog", "法律"))
        self.categoryComboBox.setItemText(4, _translate("returnBookDialog", "军事"))
        self.categoryComboBox.setItemText(5, _translate("returnBookDialog", "经济"))
        self.categoryComboBox.setItemText(6, _translate("returnBookDialog", "文化"))
        self.categoryComboBox.setItemText(7, _translate("returnBookDialog", "教育"))
        self.categoryComboBox.setItemText(8, _translate("returnBookDialog", "体育"))
        self.categoryComboBox.setItemText(9, _translate("returnBookDialog", "语言文字"))
        self.categoryComboBox.setItemText(10, _translate("returnBookDialog", "艺术"))
        self.categoryComboBox.setItemText(11, _translate("returnBookDialog", "历史"))
        self.categoryComboBox.setItemText(12, _translate("returnBookDialog", "地理"))
        self.categoryComboBox.setItemText(13, _translate("returnBookDialog", "天文学"))
        self.categoryComboBox.setItemText(14, _translate("returnBookDialog", "生物学"))
        self.categoryComboBox.setItemText(15, _translate("returnBookDialog", "医学卫生"))
        self.categoryComboBox.setItemText(16, _translate("returnBookDialog", "农业"))
        self.publisherLabel.setText(_translate("returnBookDialog", "出 版 社:"))
        self.publishDateLabel.setText(_translate("returnBookDialog", "出版日期:"))
        self.returnBookButton.setText(_translate("returnBookDialog", "确认归还"))

    def returnButtonClicked(self):
        # 获取书号，书号为空或并未借阅，则弹出错误
        # 更新Book_User表User表以及Book表
        BookId = self.bookIdEdit.text()
        # BookId为空的处理
        if (BookId == ""):
            print(QMessageBox.warning(self, "警告", "你所要还的书不存在，请查看输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 打开数据库
        # 如果未借阅
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.StudentId, BookId)
        query = db.query(sql)
        if (query == ()):
            print(QMessageBox.information(self, "提示", "您并未借阅此书，故无需归还", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 更新User表
        sql = "UPDATE User SET NumBorrowed=NumBorrowed-1 WHERE StudentId='%s'" % self.StudentId
        db.exec_(sql)

        # 更新Book表
        sql = "UPDATE Book SET NumCanBorrow=NumCanBorrow+1 WHERE BookId='%s'" % BookId
        db.exec_(sql)

        # 更新User_Book表
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            timenow, self.StudentId, BookId)
        db.exec_(sql)

        print(QMessageBox.information(self, "提示", "归还成功!", QMessageBox.Yes, QMessageBox.Yes))
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

        # 在User_Book表中找借阅记录，如果存在借阅，则更新form内容
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.StudentId, bookId)
        query = db.query(sql)
        if (query != ()):
            # 更新form内容
            sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
            query = db.query(sql)
            # 查询对应书号，如果存在就更新form
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

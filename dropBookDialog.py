# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dropBookDialog.ui'
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


class dropBookDialog(QDialog):
    drop_book_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(dropBookDialog, self).__init__(parent)

        self.setupUi()

    def setupUi(self, ):
        # self.setObjectName("dropBookDialog")
        self.resize(329, 419)
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("删除书籍")
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
        self.bookNameLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameLabel.setFont(font)
        self.bookNameLabel.setObjectName("bookNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bookNameLabel)
        self.bookNameEdit = QtWidgets.QLineEdit(self)
        self.bookNameEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameEdit.setFont(font)
        self.bookNameEdit.setStyleSheet("#363636")
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
        self.authNameEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authNameEdit.setFont(font)
        self.authNameEdit.setStyleSheet("#363636")
        self.authNameEdit.setMaxLength(10)
        self.authNameEdit.setObjectName("authNameEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.authNameEdit)
        self.categoryLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("self")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
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
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
        self.publisherLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherLabel.setFont(font)
        self.publisherLabel.setObjectName("publisherLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
        self.publisherEdit = QtWidgets.QLineEdit(self)
        self.publisherEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherEdit.setFont(font)
        self.publisherEdit.setStyleSheet("#363636")
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
        self.publishTime.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publishTime.setFont(font)
        self.publishTime.setStyleSheet("#363636")
        self.publishTime.setObjectName("publishTime")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publishTime)
        self.dropNumLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dropNumLabel.setFont(font)
        self.dropNumLabel.setObjectName("dropNumLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.dropNumLabel)
        self.dropNumEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dropNumEdit.setFont(font)
        self.dropNumEdit.setMaxLength(12)
        self.dropNumEdit.setObjectName("dropNumEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dropNumEdit)
        self.dropBookButton = QtWidgets.QPushButton(self)
        self.dropBookButton.setMaximumSize(QtCore.QSize(140, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dropBookButton.setFont(font)
        self.dropBookButton.setObjectName("dropBookButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.dropBookButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.dropBookButton.clicked.connect(self.dropBookButtonClicked)
        self.bookIdEdit.textChanged.connect(self.bookIdEditChanged)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("", "删除书籍"))
        self.titlelabel.setText(_translate("", "淘汰书籍"))
        self.bookNameLabel.setText(_translate("", "书    名:"))
        self.bookIdLabel.setText(_translate("", "书    号:"))
        self.authNameLabel.setText(_translate("", "作    者:"))
        self.categoryLabel.setText(_translate("", "分    类:"))
        self.categoryComboBox.setItemText(0, _translate("", "哲学"))
        self.categoryComboBox.setItemText(1, _translate("", "社会科学"))
        self.categoryComboBox.setItemText(2, _translate("", "政治"))
        self.categoryComboBox.setItemText(3, _translate("", "法律"))
        self.categoryComboBox.setItemText(4, _translate("", "军事"))
        self.categoryComboBox.setItemText(5, _translate("", "经济"))
        self.categoryComboBox.setItemText(6, _translate("", "文化"))
        self.categoryComboBox.setItemText(7, _translate("", "教育"))
        self.categoryComboBox.setItemText(8, _translate("", "体育"))
        self.categoryComboBox.setItemText(9, _translate("", "语言文字"))
        self.categoryComboBox.setItemText(10, _translate("", "艺术"))
        self.categoryComboBox.setItemText(11, _translate("", "历史"))
        self.categoryComboBox.setItemText(12, _translate("", "地理"))
        self.categoryComboBox.setItemText(13, _translate("", "天文学"))
        self.categoryComboBox.setItemText(14, _translate("", "生物学"))
        self.categoryComboBox.setItemText(15, _translate("", "医学卫生"))
        self.categoryComboBox.setItemText(16, _translate("", "农业"))
        self.publisherLabel.setText(_translate("", "出 版 社:"))
        self.publishDateLabel.setText(_translate("", "出版日期:"))
        self.dropNumLabel.setText(_translate("", "数    量:"))
        self.dropBookButton.setText(_translate("", "淘 汰"))

    def bookIdEditChanged(self):
        bookId = self.bookIdEdit.text()
        if (bookId == "" or len(bookId) < 6):
            self.bookNameEdit.clear()
            self.publisherEdit.clear()
            self.authNameEdit.clear()
            self.dropNumEdit.clear()
            self.publishTime.clear()

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

    def dropBookButtonClicked(self):
        bookId = self.bookIdEdit.text()
        dropNum = 0
        if (self.dropNumEdit.text() == ""):
            print(QMessageBox.warning(self, "警告", "淘汰数目为空，请检查输入，操作失败！"), QMessageBox.Yes, QMessageBox.Yes)
            return
        dropNum = int(self.dropNumEdit.text())
        sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
        query = db.query(sql)
        if (query != ()):
            if (dropNum > query[0][7] or dropNum < 0):
                print(QMessageBox.warning(self, "警告", "最多可淘汰%d本，请检查输入！" % (query[0][7]), QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
        if (query == ()):
            print(QMessageBox.warning(self, "警告", "该书本不存在，请核对再进行操作！"), QMessageBox.Yes, QMessageBox.Yes)
            return
        # 更新Book表和BuyorDrop表
        # 如果drop书目和当前库存相同，则直接删除Book记录（这里先默认当前所有书都在库存中）
        if (dropNum == query[0][6]):
            sql = "DELETE  FROM Book WHERE BookId='%s'" % (bookId)
        else:
            sql = "UPDATE BOOK SET NumStorage=NumStorage-%d,NumCanBorrow=NumCanBorrow-%d WHERE BookId='%s'" % (
                dropNum, dropNum, bookId)
        db.exec_(sql)

        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "INSERT INTO buyordrop VALUES ('%s','%s',0,%d)" % (bookId, timenow, dropNum)
        db.exec_(sql)

        print(QMessageBox.information(self, "提示", "淘汰书籍成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.drop_book_successful_signal.emit()
        self.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = dropBookDialog()
    mainMindow.show()
    sys.exit(app.exec_())

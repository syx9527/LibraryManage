# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentHome.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
import sip
import qdarkstyle
from BookStorageViewer import BookStorageViewer
from borrowBookDialog import borrowBookDialog
from returnBookDialog import returnBookDialog
from BorrowStatusViewer import BorrowStatusViewer


class StudentHome(QWidget):

    def __init__(self, studentId):
        super().__init__()
        self.StudentId = studentId
        self.setupUi()

    def setupUi(self ):
        # self.setObjectName("self")
        self.resize(1200, 600)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("layout")
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.borrowBookButton = QtWidgets.QPushButton(self)
        self.borrowBookButton.setEnabled(True)
        self.borrowBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.borrowBookButton.setFont(font)
        self.borrowBookButton.setObjectName("borrowBookButton")
        self.buttonLayout.addWidget(self.borrowBookButton)
        self.returnBookButton = QtWidgets.QPushButton(self)
        self.returnBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setObjectName("returnBookButton")
        self.buttonLayout.addWidget(self.returnBookButton)
        self.myBookStatus = QtWidgets.QPushButton(self)
        self.myBookStatus.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.myBookStatus.setFont(font)
        self.myBookStatus.setObjectName("myBookStatus")
        self.buttonLayout.addWidget(self.myBookStatus)
        self.allBookButton = QtWidgets.QPushButton(self)
        self.allBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.allBookButton.setFont(font)
        self.allBookButton.setObjectName("allBookButton")
        self.buttonLayout.addWidget(self.allBookButton)


        self.storageView = BookStorageViewer()
        self.borrowStatusView = BorrowStatusViewer(self.StudentId)
        self.allBookButton.setEnabled(False)

        self.layout.addLayout(self.buttonLayout)
        self.layout.addWidget(self.storageView)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.borrowBookButton.clicked.connect(self.borrowBookButtonClicked)
        self.returnBookButton.clicked.connect(self.returnBookButtonClicked)
        self.myBookStatus.clicked.connect(self.myBookStatusClicked)
        self.allBookButton.clicked.connect(self.allBookButtonClicked)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("StudentHome", "欢迎使用图书馆管理系统"))
        self.borrowBookButton.setText(_translate("StudentHome", "借书"))
        self.returnBookButton.setText(_translate("StudentHome", "还书"))
        self.myBookStatus.setText(_translate("StudentHome", "借阅状态"))
        self.allBookButton.setText(_translate("StudentHome", "所有书籍"))

    def borrowBookButtonClicked(self):
        borrowDialog = borrowBookDialog(self.StudentId, self)
        borrowDialog.borrow_book_success_signal.connect(self.borrowStatusView.borrowedQuery)
        borrowDialog.borrow_book_success_signal.connect(self.storageView.searchButtonClicked)
        borrowDialog.show()
        borrowDialog.exec_()
        return

    def returnBookButtonClicked(self):
        returnDialog = returnBookDialog(self.StudentId, self)
        returnDialog.return_book_success_signal.connect(self.borrowStatusView.returnedQuery)
        returnDialog.return_book_success_signal.connect(self.borrowStatusView.borrowedQuery)
        returnDialog.return_book_success_signal.connect(self.storageView.searchButtonClicked)
        returnDialog.show()
        returnDialog.exec_()

    def myBookStatusClicked(self):
        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = BookStorageViewer()
        self.borrowStatusView = BorrowStatusViewer(self.StudentId)
        self.layout.addWidget(self.borrowStatusView)
        self.allBookButton.setEnabled(True)
        self.myBookStatus.setEnabled(False)
        return

    def allBookButtonClicked(self):
        self.layout.removeWidget(self.borrowStatusView)
        sip.delete(self.borrowStatusView)
        self.borrowStatusView = BorrowStatusViewer(self.StudentId)
        self.storageView = BookStorageViewer()
        self.layout.addWidget(self.storageView)
        self.allBookButton.setEnabled(False)
        self.myBookStatus.setEnabled(True)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = StudentHome("PB15000135")
    mainMindow.show()
    sys.exit(app.exec_())

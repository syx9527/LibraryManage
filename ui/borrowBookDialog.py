# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrowBookDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_borrowBookDialog(object):
    def setupUi(self, borrowBookDialog):
        borrowBookDialog.setObjectName("borrowBookDialog")
        borrowBookDialog.resize(300, 400)
        self.formLayout = QtWidgets.QFormLayout(borrowBookDialog)
        self.formLayout.setObjectName("formLayout")
        self.titlelabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titlelabel.setFont(font)
        self.titlelabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titlelabel.setLineWidth(1)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setObjectName("titlelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titlelabel)
        self.borrowStudentLabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.borrowStudentLabel.setFont(font)
        self.borrowStudentLabel.setObjectName("borrowStudentLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.borrowStudentLabel)
        self.bookNameLabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameLabel.setFont(font)
        self.bookNameLabel.setObjectName("bookNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookNameLabel)
        self.bookNameEdit = QtWidgets.QLineEdit(borrowBookDialog)
        self.bookNameEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookNameEdit.setFont(font)
        self.bookNameEdit.setMaxLength(10)
        self.bookNameEdit.setObjectName("bookNameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookNameEdit)
        self.bookIdLabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookIdLabel.setFont(font)
        self.bookIdLabel.setObjectName("bookIdLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.bookIdLabel)
        self.bookIdEdit = QtWidgets.QLineEdit(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookIdEdit.setFont(font)
        self.bookIdEdit.setMaxLength(6)
        self.bookIdEdit.setObjectName("bookIdEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bookIdEdit)
        self.authNameLabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authNameLabel.setFont(font)
        self.authNameLabel.setObjectName("authNameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.authNameLabel)
        self.authNameEdit = QtWidgets.QLineEdit(borrowBookDialog)
        self.authNameEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authNameEdit.setFont(font)
        self.authNameEdit.setMaxLength(10)
        self.authNameEdit.setObjectName("authNameEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.authNameEdit)
        self.categoryLabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("categoryLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryComboBox = QtWidgets.QComboBox(borrowBookDialog)
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
        self.publisherLabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherLabel.setFont(font)
        self.publisherLabel.setObjectName("publisherLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
        self.publisherEdit = QtWidgets.QLineEdit(borrowBookDialog)
        self.publisherEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publisherEdit.setFont(font)
        self.publisherEdit.setMaxLength(10)
        self.publisherEdit.setObjectName("publisherEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publisherEdit)
        self.publishDateLabel = QtWidgets.QLabel(borrowBookDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publishDateLabel.setFont(font)
        self.publishDateLabel.setObjectName("publishDateLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.publishDateLabel)
        self.publishTime = QtWidgets.QDateEdit(borrowBookDialog)
        self.publishTime.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.publishTime.setFont(font)
        self.publishTime.setObjectName("publishTime")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.publishTime)
        self.borrowBookButton = QtWidgets.QPushButton(borrowBookDialog)
        self.borrowBookButton.setMaximumSize(QtCore.QSize(140, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.borrowBookButton.setFont(font)
        self.borrowBookButton.setObjectName("borrowBookButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.borrowBookButton)

        self.retranslateUi(borrowBookDialog)
        QtCore.QMetaObject.connectSlotsByName(borrowBookDialog)

    def retranslateUi(self, borrowBookDialog):
        _translate = QtCore.QCoreApplication.translate
        borrowBookDialog.setWindowTitle(_translate("borrowBookDialog", "借阅书籍"))
        self.titlelabel.setText(_translate("borrowBookDialog", "借阅书籍"))
        self.borrowStudentLabel.setText(_translate("borrowBookDialog", "借 阅 人:"))
        self.bookNameLabel.setText(_translate("borrowBookDialog", "书    名:"))
        self.bookIdLabel.setText(_translate("borrowBookDialog", "书    号:"))
        self.authNameLabel.setText(_translate("borrowBookDialog", "作    者:"))
        self.categoryLabel.setText(_translate("borrowBookDialog", "分    类:"))
        self.categoryComboBox.setItemText(0, _translate("borrowBookDialog", "哲学"))
        self.categoryComboBox.setItemText(1, _translate("borrowBookDialog", "社会科学"))
        self.categoryComboBox.setItemText(2, _translate("borrowBookDialog", "政治"))
        self.categoryComboBox.setItemText(3, _translate("borrowBookDialog", "法律"))
        self.categoryComboBox.setItemText(4, _translate("borrowBookDialog", "军事"))
        self.categoryComboBox.setItemText(5, _translate("borrowBookDialog", "经济"))
        self.categoryComboBox.setItemText(6, _translate("borrowBookDialog", "文化"))
        self.categoryComboBox.setItemText(7, _translate("borrowBookDialog", "教育"))
        self.categoryComboBox.setItemText(8, _translate("borrowBookDialog", "体育"))
        self.categoryComboBox.setItemText(9, _translate("borrowBookDialog", "语言文字"))
        self.categoryComboBox.setItemText(10, _translate("borrowBookDialog", "艺术"))
        self.categoryComboBox.setItemText(11, _translate("borrowBookDialog", "历史"))
        self.categoryComboBox.setItemText(12, _translate("borrowBookDialog", "地理"))
        self.categoryComboBox.setItemText(13, _translate("borrowBookDialog", "天文学"))
        self.categoryComboBox.setItemText(14, _translate("borrowBookDialog", "生物学"))
        self.categoryComboBox.setItemText(15, _translate("borrowBookDialog", "医学卫生"))
        self.categoryComboBox.setItemText(16, _translate("borrowBookDialog", "农业"))
        self.publisherLabel.setText(_translate("borrowBookDialog", "出 版 社:"))
        self.publishDateLabel.setText(_translate("borrowBookDialog", "出版日期:"))
        self.borrowBookButton.setText(_translate("borrowBookDialog", "确认借阅"))


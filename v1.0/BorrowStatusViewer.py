import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle
import db


class BorrowStatusViewer(QWidget):
    def __init__(self, studentId):
        super(BorrowStatusViewer, self).__init__()
        self.resize(850, 500)
        self.studentId = studentId
        self.setWindowTitle("欢迎使用图书馆管理系统")
        self.setUpUI()

    def setUpUI(self):
        # 分为两块，上方是已借未归还书，下方是已归还书
        self.layout = QVBoxLayout(self)
        # Label设置
        self.borrowedLabel = QLabel("未归还:")
        self.returnedLabel = QLabel("已归还:")
        self.borrowedLabel.setFixedHeight(32)
        self.borrowedLabel.setFixedWidth(60)
        self.returnedLabel.setFixedHeight(32)
        self.returnedLabel.setFixedWidth(60)
        font = QFont()
        font.setPixelSize(18)
        self.borrowedLabel.setFont(font)
        self.returnedLabel.setFont(font)

        # Table和Model
        self.borrowedTableView = QTableView()
        self.borrowedTableView.horizontalHeader().setStretchLastSection(True)
        self.borrowedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.borrowedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.returnedTableView = QTableView()
        self.returnedTableView.horizontalHeader().setStretchLastSection(True)
        self.returnedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.returnedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.borrowedQueryModel = QStandardItemModel()

        self.returnedQueryModel = QStandardItemModel()
        self.borrowedQueryModel.setHorizontalHeaderLabels(["书名", "书号", "作者", "分类", "出版社", "出版时间", "借出时间", ])
        self.returnedQueryModel.setHorizontalHeaderLabels(["书名", "书号", "作者", "分类", "出版社", "出版时间", "借出时间", "归还时间"])

        self.borrowedTableView.setModel(self.borrowedQueryModel)
        self.returnedTableView.setModel(self.returnedQueryModel)

        self.borrowedQuery()

        self.returnedQuery()

        self.layout.addWidget(self.borrowedLabel)
        self.layout.addWidget(self.borrowedTableView)
        self.layout.addWidget(self.returnedLabel)
        self.layout.addWidget(self.returnedTableView)
        return

    def borrowedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Auth,Category,Publisher,PublishTime,BorrowTime  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=1 AND StudentId='%s'" % self.studentId
        self.query = db.query(sql)
        self.borrowedUI()

        return

    def returnedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Auth,Category,Publisher,PublishTime,BorrowTime,ReturnTime  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=0 AND StudentId='%s'" % self.studentId
        self.query = db.query(sql)
        self.returnedUI()
        return

    def borrowedUI(self):

        for i in range(len(self.query)):
            for j in range(7):
                ite1 = QStandardItem(str(self.query[i][j]))
                self.borrowedQueryModel.setItem(i, j, ite1)
        return

    def returnedUI(self):
        for i in range(len(self.query)):
            for j in range(8):
                ite1 = QStandardItem(str(self.query[i][j]))
                self.returnedQueryModel.setItem(i, j, ite1)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.ico"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = BorrowStatusViewer("PB15000135")
    mainMindow.show()
    sys.exit(app.exec_())

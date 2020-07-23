import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CMainWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('main.ui', self)

        self.btn_userlist1.clicked.connect(self.OnBtnUserList1Clked)
        self.btn_visit1.clicked.connect(self.OnBtnVisit1Clked)
        self.btn_follow.clicked.connect(self.OnBtnFollowClked)
        self.btn_close1.clicked.connect(self.OnBtnClose1Clked)

        self.btn_userlist2.clicked.connect(self.OnBtnUserList2Clked)
        self.btn_visit2.clicked.connect(self.OnBtnVisit2Clked)
        self.btn_favourite.clicked.connect(self.OnBtnFavouriteClked)
        self.btn_close2.clicked.connect(self.OnBtnClose2Clked)

    """ slots """
    def OnBtnUserList1Clked(self):
        print('btn_userlist1')
        fname = QFileDialog.getOpenFileName(self, 'Select CSV', '', 'CSV Files (*.csv);')
        if fname[0]:
            print(fname[0])

    def OnBtnVisit1Clked(self):
        print('btn_visit1')

    def OnBtnFollowClked(self):
        print('btn_follow')

    def OnBtnClose1Clked(self):
        print('btn_close1')


    def OnBtnUserList2Clked(self):
        print('btn_userlist2')
        fname = QFileDialog.getOpenFileName(self, 'Select CSV', '', 'CSV Files (*.csv);')
        if fname[0]:
            print(fname[0])

    def OnBtnVisit2Clked(self):
        print('btn_visit2')

    def OnBtnFavouriteClked(self):
        print('btn_favourite')

    def OnBtnClose2Clked(self):
        print('btn_close2')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = CMainWnd()
    win.show()

    sys.exit(app.exec())
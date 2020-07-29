import sys
import csv
import time
import threading

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import libraries.product as product
import libraries.shop as shop

def shop_visit(shop_url, users, idle_time):
    for user in users:
        username = user[0]
        password = user[1]
        sh = shop.Shop(shop_url, username, password)
        sh.visit(idle_time)

def shop_follow(shop_url, users, idle_time):
    for user in users:
        username = user[0]
        password = user[1]
        sh = shop.Shop(shop_url, username, password)
        sh.follow(idle_time)

def product_visit(product_url, users, idle_time):
    for user in users:
        username = user[0]
        password = user[1]
        prod = product.Product(product_url, username, password)
        prod.visit(idle_time)

def product_favorite(product_url, users, idle_time):
    for user in users:
        username = user[0]
        password = user[1]
        prod = product.Product(product_url, username, password)
        prod.favorite(idle_time)

class CMainWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('main.ui', self)

        self.le_visit_idle.setValidator(QIntValidator(1, 100, self))
        self.le_visitfollow_idle.setValidator(QIntValidator(1, 100, self))
        self.le_visitfavourite_idle.setValidator(QIntValidator(1, 100, self))

        self.Shop_users = []
        self.Product_users = []

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
        fname = QFileDialog.getOpenFileName(self, 'Select CSV', '', 'CSV Files (*.csv);')
        if fname[0]:
            self.le_userlist1.setText(fname[0])
            self.Shop_users = []
            with open(fname[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        self.Shop_users.append(row)
                        line_count += 1

    def OnBtnVisit1Clked(self):
        shop_url = self.le_shop_url.text()
        idle_time = int(self.le_visit_idle.text())

        if idle_time < 30:
            idle_time = 30
        elif idle_time > 100:
            idle_time = 100

        if not shop_url:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the shop url.", QMessageBox.Yes, QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        if not self.Shop_users:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the user list file path.", QMessageBox.Yes,
                                               QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        threading.Thread(target=shop_visit, args=(shop_url, self.Shop_users, idle_time,)).start()

    def OnBtnFollowClked(self):
        shop_url = self.le_shop_url.text()
        idle_time = int(self.le_visitfollow_idle.text())

        if idle_time < 30:
            idle_time = 30
        elif idle_time > 100:
            idle_time = 100

        if not shop_url:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the shop url.", QMessageBox.Yes, QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        if not self.Shop_users:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the user list file path.", QMessageBox.Yes,
                                               QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        threading.Thread(target=shop_follow, args=(shop_url, self.Shop_users, idle_time,)).start()

    def OnBtnClose1Clked(self):
        self.close()


    def OnBtnUserList2Clked(self):
        fname = QFileDialog.getOpenFileName(self, 'Select CSV', '', 'CSV Files (*.csv);')
        if fname[0]:
            self.le_userlist2.setText(fname[0])
            self.Product_users = []
            with open(fname[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        self.Product_users.append(row)
                        line_count += 1


    def OnBtnVisit2Clked(self):
        product_url = self.le_product_url.text()
        idle_time = int(self.le_visitfavourite_idle.text())

        if idle_time < 30:
            idle_time = 30
        elif idle_time > 100:
            idle_time = 100

        if not product_url:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the product url.", QMessageBox.Yes, QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        if not self.Product_users:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the user list file path.", QMessageBox.Yes, QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        threading.Thread(target=product_visit, args=(product_url, self.Product_users, idle_time,)).start()

    def OnBtnFavouriteClked(self):
        product_url = self.le_product_url.text()
        idle_time = int(self.le_visitfavourite_idle.text())

        if idle_time < 30:
            idle_time = 30
        elif idle_time > 100:
            idle_time = 100

        if not product_url:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the product url.", QMessageBox.Yes, QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        if not self.Product_users:
            buttonReply = QMessageBox.question(self, 'Message', "Please input the user list file path.", QMessageBox.Yes, QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                return
            else:
                return

        threading.Thread(target=product_favorite, args=(product_url, self.Product_users, idle_time,)).start()

    def OnBtnClose2Clked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = CMainWnd()
    win.show()

    sys.exit(app.exec())
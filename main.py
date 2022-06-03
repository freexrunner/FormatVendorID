#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:55:09 2022

@author: freexrunner
"""

import sys
import time

from PyQt5 import uic
# from threading import Thread
from writer import Writer
from vendor_id_ui import *

class FormatVendorID(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.process_status = 'Stop'

        self.radioGroup = QtWidgets.QButtonGroup()
        self.radioGroup.addButton(self.ui.model_snr, 0)
        self.radioGroup.addButton(self.ui.model_bo, 1)
        # self.model = self.radioGroup.checkedId()
        self.ui.button_start.clicked.connect(self.start)

    def check_input_data(self):
        # добавить проверку корректности исходных значений
        int_name = self.ui.int_name.text()
        ip_address = self.ui.ip_address.text()
        username = self.ui.input_username.text()
        password = self.ui.input_password.text()
        self.model = self.radioGroup.checkedId()
        self.writer = Writer(int_name, ip_address, username, password)

    def start(self):
        self.check_input_data()
        if self.writer.interface_status():
            while delay > 0:
                if self.writer.check_host_connect():
                    self.updateUI("Подключен терминал. Выполняется настройка")
                    self.writer.start_write(self.model)
                    self.updateUI("Настройка завершена. Подключите следующий терминал")
                    delay = 0
                else:
                    self.updateUI(f"Ожидание подключения терминала: {str(delay)}")
                    time.sleep(1)
                    delay -= 1
        else:
            self.updateUI("Нет подключения к сетевому интерфейсу")


    def updateUI(self, message):
        self.ui.out_text.setText(message)
        # pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = FormatVendorID()
    myapp.show()
    sys.exit(app.exec_())

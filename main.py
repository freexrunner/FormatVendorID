#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:55:09 2022

@author: freexrunner
"""

import sys
import time
from PyQt5 import QtCore
# from threading import Thread
from writer import Writer
from interface_thread import InterfaceStatusThread
from write_tread import WriterThread
# from write_tread import *
from vendor_id_ui import *


class FormatVendorID(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.interface_thread = None
        self.model = None
        self.password = None
        self.username = None
        self.ip_address = None
        self.int_name = None
        self.write_thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.running = False

        self.radioGroup = QtWidgets.QButtonGroup()
        self.radioGroup.addButton(self.ui.model_snr, 0)
        self.radioGroup.addButton(self.ui.model_bo, 1)
        # self.model = self.radioGroup.checkedId()
        self.ui.button_start.clicked.connect(self.start)
        self.ui.out_text.setText("Подключите терминал и нажмите Start")

    def check_input_data(self):
        # добавить проверку корректности исходных значений
        self.int_name = self.ui.int_name.text()
        self.ip_address = self.ui.ip_address.text().replace(',', '.')
        self.username = self.ui.input_username.text()
        self.password = self.ui.input_password.text()
        self.model = self.radioGroup.checkedId()

        if len(self.int_name) == 0 or len(self.ip_address) == 0 or len(self.username) == 0 or len(self.password) == 0:
            msg_empty = QtWidgets.QMessageBox()
            msg_empty.setWindowTitle('Ошибка ввода данных')
            msg_empty.setText('Укажите все исходные данные')
            msg_empty.setIcon(msg_empty.Warning)
            msg_empty.exec()
            return False
        else:
            return True

    def start(self):
        if self.check_input_data():
            self.write_thread = WriterThread(self.int_name, self.ip_address, self.username, self.password, self.model)
            self.interface_thread = InterfaceStatusThread(self.int_name)
            self.interface_thread.interface_signal.connect(self.update_interface_status)
            self.write_thread.message_signal.connect(self.update_message)

            self.interface_thread.start()
            self.write_thread.start()

    def update_interface_status(self, int_status_str):
        self.ui.int_state.setText(int_status_str)

    def update_message(self, message):
        self.ui.out_text.setText(message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = FormatVendorID()
    myapp.show()
    sys.exit(app.exec_())

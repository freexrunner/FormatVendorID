#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:55:09 2022

@author: freexrunner
"""

import sys
import time
# from PyQt5 import uic
# from threading import Thread
from writer import Writer
from write_tread import *
from vendor_id_ui import *

class FormatVendorID(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ready_to_start = False

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
        self.ready_to_start = True

    def start(self):
        self.updateUI("")
        self.check_input_data()
        self.updateUI("Waiting to connect")

        self.test_thread = TestTread(self.writer.int_name)


        if self.ready_to_start and self.wait_to_connect():
            self.updateUI("Terminal connected. Writing")
            self.writer.start_write(self.model)
            self.updateUI("Writing complete! Connect next terminal and click Start button")
            self.ready_to_start = False

    def wait_to_connect(self):
        if self.writer.interface_status():
            delay = 5
            while delay > 0:
                if self.writer.check_host_connect():
                    return True
                    break
                else:
                    time.sleep(1)
                    delay -= 1
            self.updateUI("Terminal is not available")
            return False
        else:
            self.updateUI("Not connected")
            return False

    def updateUI(self, message):
        self.ui.out_text.setText(message)
        # pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = FormatVendorID()
    myapp.show()
    sys.exit(app.exec_())

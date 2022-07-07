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
from write_tread import WritterThread
# from write_tread import *
from vendor_id_ui import *


class FormatVendorID(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.model = None
        self.password = None
        self.username = None
        self.ip_address = None
        self.int_name = None
        self.write_thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ready_to_start = False
        self.running = False

        self.radioGroup = QtWidgets.QButtonGroup()
        self.radioGroup.addButton(self.ui.model_snr, 0)
        self.radioGroup.addButton(self.ui.model_bo, 1)
        # self.model = self.radioGroup.checkedId()
        self.ui.button_start.clicked.connect(self.start)

    def check_input_data(self):
        # добавить проверку корректности исходных значений
        self.int_name = self.ui.int_name.text()
        self.ip_address = self.ui.ip_address.text()
        self.username = self.ui.input_username.text()
        self.password = self.ui.input_password.text()
        self.model = self.radioGroup.checkedId()
        # self.writer = Writer(ip_address, username, password)
        self.ready_to_start = True

    def start(self):
        # запуск потока writerThread
        self.check_input_data()
        self.write_thread = WritterThread(self.int_name, self.ip_address, self.username, self.password, self.model)
        self.write_thread.message_signal.connect(self.update_message)
        self.write_thread.interface_signal.connect(self.update_interface_status)
        self.write_thread.start()

        # # запуск потока interface_thread
        # if not self.running:
        #     self.check_input_data()
        #     self.interface_thread = InterfaceStatusThread(self.int_name)
        #     self.interface_thread.interface_signal.connect(self.update_interface_status)
        #     self.interface_thread.start()
        #     self.ui.button_start.setText("Stop")
        #     self.running = True
        # else:
        #     self.interface_thread.running = False
        #     self.ui.button_start.setText("Start")
        #     self.running = False

        # self.check_input_data()
        # # self.updateUI("Waiting to connect")
        # self.test_thread = InterfaceStatusThread(self.int_name)
        # self.test_thread.test_signal.connect(self.updateUI)
        # self.test_thread.start()

    ##########################################################################
    # Одиночная запись по кнопке

    # self.check_input_data()
    # self.update_message("")
    # if self.ready_to_start and self.wait_to_connect():
    #     self.update_message("Terminal connected. Writing")
    #     self.writer.start_write(self.model)
    #     self.update_message("Writing complete! Connect next terminal and click Start button")
    #     self.ready_to_start = False

    ##########################################################################

    # def wait_to_connect(self):
    #     if self.writer.interface_status():
    #         delay = 5
    #         while delay > 0:
    #             if self.writer.check_host_connect():
    #                 return True
    #                 break
    #             else:
    #                 time.sleep(1)
    #                 delay -= 1
    #         self.update_interface_status("Terminal is not available")
    #         return False
    #     else:
    #         self.update_interface_status("Not connected")
    #         return False

    def update_interface_status(self, int_status_str):
        self.ui.int_state.setText(int_status_str)

    def update_message(self, message):
        self.ui.out_text.setText(message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = FormatVendorID()
    myapp.show()
    sys.exit(app.exec_())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:55:09 2022

@author: freexrunner
"""

import sys
from PyQt5 import uic

from PaperbackWriter import PaperbackWriter
from vendor_id_ui import *


class FormatVendorID(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        #self.writer = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.radioGroup = QtWidgets.QButtonGroup()
        self.radioGroup.addButton(self.ui.model_snr, 0)
        self.radioGroup.addButton(self.ui.model_bo, 1)
        #self.model = self.radioGroup.checkedId()

        self.ui.button_start.clicked.connect(self.start)



    def check_input_data(self):
        int_name = self.ui.int_name.text()
        ip_address = self.ui.ip_address.text()
        username = self.ui.input_username.text()
        password = self.ui.input_password.text()
        self.writer = PaperbackWriter(int_name, ip_address, username, password)


    def start(self):
        self.check_input_data()
        test_result = self.writer.start_write(self.radioGroup.checkedId())
        self.updateUI()
        #pass

    def updateUI(self):
        self.ui.out_text.setText("string_test")
        #pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = FormatVendorID()
    myapp.show()
    sys.exit(app.exec_())

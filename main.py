#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:55:09 2022

@author: freexrunner
"""

import sys
from PyQt5 import uic
from vendor_id import *


class FormatVendorID(QtWidgets.QMainWidow) :
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = FormatVendorID()
    myapp.show()
    sys.exit(app.exec_())

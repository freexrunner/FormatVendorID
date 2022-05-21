#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:55:09 2022

@author: freexrunner
"""

import sys



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = CableCalcMain()
    myapp.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:06:26 2021

@author: cleme
"""

import graphicinterface as GUI
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = GUI.GraphicInterface(w)
    w.show()
    sys.exit(app.exec_())
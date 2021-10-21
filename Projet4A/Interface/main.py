# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:06:26 2021

@author: cleme
"""
from PyQt5 import QtWidgets
import application, windows, settings
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    setting = settings.settings((app.primaryScreen().size().width(),app.primaryScreen().size().height()),win)
    win.resize(260,250)
    win.show()
    sys.exit(app.exec_())
    """
    
    #w = windows.windows((app.primaryScreen().size().width(),app.primaryScreen().size().height()))
    #w.setCentralWidget(setting.getWidget())
    #w.showWindow()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = settings.settings((800,600),MainWindow)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""
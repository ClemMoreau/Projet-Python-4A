# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:06:26 2021

@author: cleme
"""
from PyQt5 import QtWidgets
import application, windows, settings
import sys

if __name__ == "__main__":

    mainApp = application.application()
    maxScreenSize = (mainApp.getApp().primaryScreen().size().width()
                     ,mainApp.getApp().primaryScreen().size().height())
    
    mainWindow = windows.windows((260,250))
    
    settingWidget = settings.settings(maxScreenSize,mainWindow.getWindow())
    
    mainWindow.modifyWindow()
    mainWindow.showWindow()
    
    mainApp.exitApp()
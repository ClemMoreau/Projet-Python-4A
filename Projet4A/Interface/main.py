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
    maxScreenSize = (mainApp.get_app().primaryScreen().size().width()
                     ,mainApp.get_app().primaryScreen().size().height())
    
    mainWindow = windows.windows((260,250))
    
    settingWidget = settings.settings(maxScreenSize,mainWindow.get_window())
    
    mainWindow.modify_window()
    mainWindow.show_window()
    
    mainApp.exit_app()
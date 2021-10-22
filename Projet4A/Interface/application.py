# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:30:11 2021

@author: cleme
"""

import sys
from PyQt5 import QtWidgets

class application(object):
    
            #############
            #CONSTRUCTOR#
            #############    
            
    def __init__(self):
        self.mainApplication = QtWidgets.QApplication(sys.argv)
        self.screenWidth = self.mainApplication.primaryScreen().size().width()
        self.screenHeight = self.mainApplication.primaryScreen().size().height()
            
            #########
            #GETTERS#
            #########
    
    #useless?
    def getApp(self):
        return self.mainApplication

    def getScreenHeight(self):
        return self.screenHeight
        
    def getScreenWidth(self):
        return self.screenWidth
 
            #########
            #SETTERS#
            #########
            
    def setApp(self, application):
        self.mainApplication = application

    def setScreenWidth(self, size):
        self.screenHeight = size        
    
    def setScreenHeight(self, size):
        self.screenHeight = size
        
            #########
            #METHODS#
            #########
        
    def exitApp(self):
        sys.exit(self.mainApplication.exec_())
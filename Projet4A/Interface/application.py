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
    def get_app(self):
        return self.mainApplication

    def get_screen_height(self):
        return self.screenHeight
        
    def get_screen_width(self):
        return self.screenWidth
 
            #########
            #SETTERS#
            #########
            
    def set_app(self, application):
        self.mainApplication = application

    def set_screen_width(self, size):
        self.screenHeight = size        
    
    def set_screen_height(self, size):
        self.screenHeight = size
        
            #########
            #METHODS#
            #########
        
    def exit_app(self):
        sys.exit(self.mainApplication.exec_())
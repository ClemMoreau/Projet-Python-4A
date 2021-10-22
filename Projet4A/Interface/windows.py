# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:38:33 2021

@author: cleme
"""

from PyQt5 import QtWidgets

class windows(object):
    
            #############
            #CONSTRUCTOR#
            ############# 
            
   #Changer size (tuple) en deux int ?
    def __init__(self, size):
        self.window = QtWidgets.QMainWindow()
        self.windowWidth = size[0]
        self.windowHeight = size[1]
        
            #########
            #GETTERS#
            #########
            
    def getWindow(self):
        return self.window
    
    def getWindowWidth(self):
        return self.windowWidth
        
    def getWindowHeight(self):
        return self.windowHeight
    
            #########
            #SETTERS#
            #########
    
    def setWindow(self, newWindow):
        self.window = newWindow
    
    def setWindowsWidth(self, size):
        self.windowWidth = size
    
    def setWindowsHeight(self, size):
        self.windowHeight = size
        
    def setCentralWidget(self, widget):
        self.window.setCentralWidget(widget)
        
        
            #########
            #METHODS#
            #########
            
    def modifyWindow(self):
        self.window.resize(self.windowWidth, self.windowHeight)
                    
    def showWindow(self):
        self.window.show()
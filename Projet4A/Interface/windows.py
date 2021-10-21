# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:38:33 2021

@author: cleme
"""

from PyQt5 import QtWidgets

class windows(QtWidgets.QMainWindow):
    
            #############
            #CONSTRUCTOR#
            ############# 
            
   #Changer size (tuple) en deux int ?
    def __init__(self, size):
        QtWidgets.QMainWindow.__init__(self)
        self.window = QtWidgets.QMainWindow()
        self.windowMaxWidth = size[0]
        self.windowMaxHeight = size[1]
        
            #########
            #GETTERS#
            #########
            
    def getWindow(self):
        return self.window
                
    def getWindowMaxWidth(self):
        return self.windowMaxWidth
        
    def getWindowMaxHeight(self):
        return self.windowMaxHeight
    
            #########
            #SETTERS#
            #########
            
    def setWindow(self, newWindow):
        self.window = newWindow
    
    def setWindowMaxWidth(self, size):
        self.windowMaxWidth = size
    
    def setWindowMaxHeight(self, size):
        self.windowMaxHeight = size
        
    def setCentralWidget(self, widget):
        self.window.setCentralWidget(widget)
        
            #########
            #METHODS#
            #########
            
    def modifyWindow(self):
        self.window.resize(self.windowMaxWidth // 5, self.windowMaxHeight // 5)
            
    def showWindow(self):
        self.window.show()
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
            
    def get_window(self):
        return self.window
    
    def get_window_width(self):
        return self.windowWidth
        
    def get_window_height(self):
        return self.windowHeight
    
            #########
            #SETTERS#
            #########
    
    def set_window(self, newWindow):
        self.window = newWindow
    
    def set_windows_width(self, size):
        self.windowWidth = size
    
    def set_windows_weight(self, size):
        self.windowHeight = size
        
    def set_central_widget(self, widget):
        self.window.setCentralWidget(widget)
        
        
            #########
            #METHODS#
            #########
            
    def modify_window(self):
        self.window.resize(self.windowWidth, self.windowHeight)
                    
    def show_window(self):
        self.window.show()
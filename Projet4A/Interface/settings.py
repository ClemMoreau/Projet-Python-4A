# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:49:48 2021

@author: cleme
"""

import pavage as pav
from PyQt5 import QtWidgets, QtCore

class settings(object):
    
        #############
        #CONSTRUCTOR#
        ############# 
    
    #Changer size (tuple) en deux int ?
    def __init__(self, size, win):
        self.nbPolyPerLine = 0
        self.typeOfPoly = ""
        self.widget = QtWidgets.QWidget()
        self.widgetMaxWidth = size[0]
        self.widgetMaxHeight = size[1]
        
        win.resize(size[0],size[1])
        win.setCentralWidget(self.widget)

        self.set_graphic_interface()
        
        self.win = win
            
            #########
            #GETTERS#
            #########
    
    def get_nb_polygon(self):
        return self.nbPolyPerLine
    
    def get_type_of_poly(self):
        return self.typeOfPoly

    def get_widget(self):
        return self.widget
    
    def get_widget_max_width(self):
        return self.widgetMaxWidth
    
    def get_widget_max_height(self):
        return self.widgetMaxHeights

            #########
            #SETTERS#
            #########
            
    def set_type_of_poly(self, polyName):
        self.typeOfPoly = polyName        
    
    def set_nb_polygon(self, nb):
        if(nb >= 0):
            self.nbPolyPerLine = nb
    
    def set_widget(self, widget):
        self.widget = widget
        
    def set_widget_max_width(self, size):
        if(size >= 0):
            self.widgetMaxWidth = size
            
    def set_widget_max_height(self, size):
        if(size >= 0):
            self.widgetMaxHeight= size
        
            #########
            #METHODS#
            #########
            
    def set_graphic_interface(self):
        
        #To set same size with the window
        self.widget.resize(260,250)
        
        #Text label TypeOfPoly
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 200, 20))
        self.label.setObjectName("label")
        self.label.setText("Please choose a type of polygon to paint : ")
        
        #Combo Box containing TypeOfPoly
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(50, 40, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Triangle")
        self.comboBox.addItem("Square")
        self.comboBox.addItem("Hexagon")
        
        #Spin box to select number of polygon per line [5;+∞[
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setGeometry(QtCore.QRect(200, 80, 42, 22))
        self.spinBox.setMinimum(5)
        self.spinBox.setObjectName("spinBox")
        
        #Text label to chose number of polygon per line
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 181, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Please choose the number of polygon per line : ")
        
        #Pushbutton to call the click function 
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(90, 150, 90, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Draw !")
        self.pushButton.clicked.connect(self.click)
        
    def click(self):       
        
        self.set_nb_polygon(self.spinBox.value())
       
        self.win.setCentralWidget(pav.Pavage((self.widgetMaxWidth,self.widgetMaxHeight),self.get_nb_polygon(),self.comboBox.currentText()))
        self.win.show()
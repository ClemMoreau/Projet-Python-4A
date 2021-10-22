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

        self.setGraphicInterface()
        
        self.win = win
            
            #########
            #GETTERS#
            #########
    
    def getNbPolygone(self):
        return self.nbPolyPerLine
    
    def getTypeOfPoly(self):
        return self.typeOfPoly

    def getWidget(self):
        return self.widget
    
    def getWidgetMaxWidth(self):
        return self.widgetMaxWidth
    
    def getWidgetMaxHeight(self):
        return self.widgetMaxHeights

            #########
            #SETTERS#
            #########
            
    def setTypeOfPoly(self, polyName):
        self.typeOfPoly = polyName        
    
    def setNbPolygone(self, nb):
        if(nb >= 0):
            self.nbPolyPerLine = nb
    
    def setWidget(self, widget):
        self.widget = widget
        
    def setWidgetMaxWidth(self, size):
        if(size >= 0):
            self.widgetMaxWidth = size
            
    def setWidgetMaxHeight(self, size):
        if(size >= 0):
            self.widgetMaxHeight= size
        
            #########
            #METHODS#
            #########
            
    def setGraphicInterface(self):
        
        #To set same size with the window
        #self.widget.resize(260,250)
        
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
        self.pushButton.setText("Dessiner !")
        self.pushButton.clicked.connect(self.click)
        
    def click(self):       
        
        self.setNbPolygone(self.spinBox.value())
       
        self.win.setCentralWidget(pav.Pavage((self.widgetMaxWidth,self.widgetMaxHeight),self.getNbPolygone(),self.comboBox.currentText()))
        self.win.show()
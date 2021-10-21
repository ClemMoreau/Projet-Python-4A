# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:54:22 2021

@author: cleme
"""


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import pavage as pav

class GraphicInterface(object):
    
    def __init__(self, size):
       # super.__init__(widget)
       self.widget = QtWidgets.QWidget()
       self.setGraphicInterface(self.widget)
       self.size = size
    
    def setGraphicInterface(self, widget):
        widget.resize(250, 300)
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 20))
        self.label.setObjectName("label")
        self.label.setText("Veuillez choisir le polygone à dessiner : ")
        self.comboBox = QtWidgets.QComboBox(widget)
        self.comboBox.setGeometry(QtCore.QRect(50, 40, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Triangle")
        self.comboBox.addItem("Carrée")
        self.comboBox.addItem("Hexagone")
        self.spinBox = QtWidgets.QSpinBox(widget)
        self.spinBox.setGeometry(QtCore.QRect(200, 80, 42, 22))
        self.spinBox.setMinimum(5)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 181, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Veuillez choisi le nombre de polygone \n en horizontale : ")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(90, 150, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click)
        self.pushButton.setText("Dessiner !")
    
    def click(self):
        print("pressed")
        win = QtWidgets.QMainWindow()
        pavage = pav.Pavage(self.size)
        win.setCentralWidget(pavage)
        win.show()
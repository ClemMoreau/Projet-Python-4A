# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:41:03 2021

@author: cleme
"""

from PyQt5 import QtWidgets, QtGui, QtCore, Qt

class rect:
    def __init__(self):
        self.rect = QtGui.QPolygonF()
        self.rect << QtCore.QPoint(10,100)
        self.rect << QtCore.QPoint(200,100)
        self.rect << QtCore.QPoint(200,200)
        self.rect << QtCore.QPoint(10,200)

    

t = rect()
t.rect.insert(0,QtCore.QPoint(150,400))
for i in range(0,t.rect.count()):
    print(t.rect.at(i))
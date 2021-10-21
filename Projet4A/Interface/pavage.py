# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:22:13 2021

@author: cleme
"""

from PyQt5 import QtWidgets, QtGui, QtCore


class Pavage(QtWidgets.QWidget):
    
    def __init__(self,size):
        super().__init__()
        self.size = size
      
    #evenement QPaintEvent
    def paintEvent(self, event):   # event de type QPaintEvent
     
    # recupere le QPainter du widget
        painter = QtGui.QPainter(self)  
        nbH = 24
        taille = self.size//nbH
        for k in range(0,nbH+1):
            for m in range(0,nbH+1):
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0+k*taille,0+m*taille)
                polygon << QtCore.QPoint(taille+k*taille,0+m*taille)
                polygon << QtCore.QPoint(taille+k*taille,taille+m*taille)
                polygon << QtCore.QPoint(0+k*taille,taille+m*taille)
                painter.drawPolygon(polygon)
        return
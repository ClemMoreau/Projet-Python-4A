# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:11:51 2021

@author: jeana
"""
from PyQt5 import QtWidgets, QtGui, QtCore
import math


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
                #Si m est pair, on dessine des triangles oreintés vers le bas
                if (m % 2 == 0) :
                    
                    polygon = QtGui.QPolygon()
                    polygon << QtCore.QPoint(0+k*taille,0+m*taille * ((math.sqrt(3))/2))
                    polygon << QtCore.QPoint(taille+k*taille,0+m*taille * ((math.sqrt(3))/2))
                    polygon << QtCore.QPoint(0.5*taille + k*taille,taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2)
                    painter.drawPolygon(polygon)
                    
                    
                    
                else :
                    #Si m est impair on  dessine des trainlge orienté vers le haut
                    polygon << QtCore.QPoint(0.5*taille + k*taille,0+m*taille * ((math.sqrt(3))/2))
                    polygon << QtCore.QPoint(0 + k * taille, taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2 )
                    polygon << QtCore.QPoint(taille + k * taille, taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2 )
                    painter.drawPolygon(polygon)
                
                #A chaque itération on dessine les segments qui finissent les triangles non tracés
                painter.drawLine(0,0+m*taille * ((math.sqrt(3))/2),0.5*taille,0+m*taille * ((math.sqrt(3))/2))
                painter.drawLine(0.5*taille + k*taille, taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2,0.5*taille + (k+1)*taille,taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2)
                
        return
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:22:13 2021

@author: cleme
"""
import math
from PyQt5 import QtWidgets, QtGui, QtCore


class Pavage(QtWidgets.QWidget):
    
    def __init__(self,size,numberPolygonPerLine, typeofPolygon):
        super().__init__()
        self.size = size
        self.numberPolygonPerLine = numberPolygonPerLine
        self.length = self.size[0]//self.numberPolygonPerLine
        self.numberPolygonPerColumn = self.size[0]//self.length
        self.typeofPolygon = typeofPolygon
        self.listOfPolygon = []        
      
    #evenement QPaintEvent
    def paintEvent(self, event):   # event de type QPaintEvent
     
        # recupere le QPainter du widget
        
        if (self.typeofPolygon == "Square"):
            self.drawRect()  
        if (self.typeofPolygon == "Triangle"):
            self.drawTriangle()
        if (self.typeofPolygon == "Hexagon"):
            self.drawHexagon()
        return
    
    def drawRect(self):
        
            painter = QtGui.QPainter(self)
            
            for abscissa in range(-1, (self.numberPolygonPerLine + 1)):
                if (abscissa % 2 == 0):
                    paint = True
                else:
                    paint = False
                    
                for ordinate in range(-1, (self.numberPolygonPerColumn + 1)):
                    if(paint):
                        polygon = QtGui.QPolygonF()
                        #Top-Left point
                        polygon << QtCore.QPointF(0 + (abscissa * self.length),
                                                 0 + (ordinate * self.length))
                        #Top-Right point
                        polygon << QtCore.QPointF(self.length + (abscissa * self.length),
                                                 0 + (ordinate * self.length))
                        #Bot-right point
                        polygon << QtCore.QPointF(self.length + (abscissa * self.length),
                                                 self.length + (ordinate * self.length))
                        #Bot-left point
                        polygon << QtCore.QPointF(0 + (abscissa * self.length),
                                                 self.length + (ordinate * self.length))
                        painter.drawPolygon(polygon)
                        self.listOfPolygon.append(polygon)
                    paint = not paint
        
    def drawTriangle(self):
        
        painter = QtGui.QPainter(self)  
        
        for k in range(0,self.numberPolygonPerLine+1):
            for m in range(0,self.numberPolygonPerColumn+1):               
                #Si m est pair, on dessine des triangles oreintés vers le bas
                if (m % 2 == 0) :
                    
                    polygon = QtGui.QPolygon()
                    polygon << QtCore.QPoint(0+k*self.length,0+m*self.length * ((math.sqrt(3))/2))
                    polygon << QtCore.QPoint(self.length+k*self.length,0+m*self.length * ((math.sqrt(3))/2))
                    polygon << QtCore.QPoint(0.5*self.length + k*self.length,self.length * m * ((math.sqrt(3))/2) + self.length*(math.sqrt(3))/2)
                    painter.drawPolygon(polygon)
                    
                else :
                    #Si m est impair on  dessine des trainlge orienté vers le haut
                    polygon = QtGui.QPolygon()
                    polygon << QtCore.QPoint(0.5*self.length + k*self.length,0+m*self.length * ((math.sqrt(3))/2))
                    polygon << QtCore.QPoint(0 + k * self.length, self.length * m * ((math.sqrt(3))/2) + self.length*(math.sqrt(3))/2 )
                    polygon << QtCore.QPoint(self.length + k * self.length, self.length * m * ((math.sqrt(3))/2) + self.length*(math.sqrt(3))/2 )
                    painter.drawPolygon(polygon)
                    
                self.listOfPolygon.append(polygon)
                
                #A chaque itération on dessine les segments qui finissent les triangles non tracés
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0,0+m*self.length * ((math.sqrt(3))/2))
                polygon << QtCore.QPoint(0.5*self.length,0+m*self.length * ((math.sqrt(3))/2))
                painter.drawPolygon(polygon)
                
                self.listOfPolygon.append(polygon)

                
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0.5*self.length + k*self.length, self.length * m * ((math.sqrt(3))/2) + self.length*(math.sqrt(3))/2)
                polygon << QtCore.QPoint(0.5*self.length + (k+1)*self.length,self.length * m * ((math.sqrt(3))/2) + self.length*(math.sqrt(3))/2)
                painter.drawPolygon(polygon)
                self.listOfPolygon.append(polygon)
                    
    def drawHexagon(self):
        painter = QtGui.QPainter(self)  
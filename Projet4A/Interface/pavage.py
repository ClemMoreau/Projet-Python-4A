# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:22:13 2021

@author: cleme
"""
import math
from PyQt5 import QtWidgets, QtGui, QtCore

TRIANGLE_CONST = math.sqrt(3)/2


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
            self.draw_rect()  
        if (self.typeofPolygon == "Triangle"):
            self.draw_triangle()
        if (self.typeofPolygon == "Hexagon"):
            self.draw_hexagon()
        return
    
    def draw_rect(self):
        
            painter = QtGui.QPainter(self)
            
            for i in range(-1, (self.numberPolygonPerLine + 1)):
            
                
                if (i % 2 == 0):
                    paint = True
                else:
                    paint = False
                    
                for j in range(-1, (self.numberPolygonPerColumn + 1)):
                    if(paint):
                        polygon = QtGui.QPolygonF()
                        
                        abscissa = (i * self.length)
                        ordinate = (j * self.length)
                        
                        #Top-Left point
                        polygon << QtCore.QPointF(abscissa, ordinate)
                        #Top-Right point
                        polygon << QtCore.QPointF(self.length + abscissa, ordinate)
                        #Bot-right point
                        polygon << QtCore.QPointF(self.length + abscissa, self.length + ordinate)
                        #Bot-left point
                        polygon << QtCore.QPointF(abscissa, self.length + ordinate)
                        
                        painter.drawPolygon(polygon)
                        
                        self.listOfPolygon.append(polygon)
                    paint = not paint
        
    def draw_triangle(self):
        
        painter = QtGui.QPainter(self)  
        
        for i in range(-1,self.numberPolygonPerLine+1):
            
            for j in range(-1,self.numberPolygonPerColumn+1):               
            
                iLength = i * self.length
                jLength = j * self.length

                #Si j est pair, on dessine des triangles oreintés vers le bas
                if (j % 2 == 0) :
                    
                    polygon = QtGui.QPolygon()
                            
                    polygon << QtCore.QPoint(iLength, jLength * TRIANGLE_CONST)
                    polygon << QtCore.QPoint(self.length + iLength, jLength * TRIANGLE_CONST)
                    polygon << QtCore.QPoint(0.5 * self.length + iLength, (jLength + self.length) * TRIANGLE_CONST)
                    painter.drawPolygon(polygon)
                    
                else :
                    #Si j est impair on  dessine des trainlge orienté vers le haut
                    polygon = QtGui.QPolygon()
                    
                    polygon << QtCore.QPoint(0.5 * self.length + iLength, jLength * TRIANGLE_CONST)
                    polygon << QtCore.QPoint(iLength, (jLength + self.length) * TRIANGLE_CONST)
                    polygon << QtCore.QPoint(self.length + iLength, (jLength + self.length) * TRIANGLE_CONST)
                    painter.drawPolygon(polygon)
                    
                self.listOfPolygon.append(polygon)
                
                #A chaque itération on dessine les segments qui finissent les triangles non tracés
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0, jLength * TRIANGLE_CONST)
                polygon << QtCore.QPoint(0.5 *self.length, jLength * TRIANGLE_CONST)
                painter.drawPolygon(polygon)
                
                self.listOfPolygon.append(polygon)

                
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0.5 * self.length + iLength, (jLength + self.length) * TRIANGLE_CONST)
                polygon << QtCore.QPoint(1.5 * self.length + iLength, (jLength + self.length) * TRIANGLE_CONST)
                painter.drawPolygon(polygon)
                self.listOfPolygon.append(polygon)
                    
    def draw_hexagon(self):
        painter = QtGui.QPainter(self)  
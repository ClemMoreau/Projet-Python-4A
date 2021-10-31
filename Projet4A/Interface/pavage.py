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
        
        self.point_to_add = False
        self.first_time = True
      
    #evenement QPaintEvent
    def paintEvent(self, event):   # event de type QPaintEvent
     
        # recupere le QPainter du widget
        if (self.typeofPolygon == "Square" and self.first_time):
            self.draw_rect()  
        if (self.typeofPolygon == "Triangle" and self.first_time):
            self.draw_triangle()
        if (self.typeofPolygon == "Hexagon" and self.first_time):
            self.draw_hexagon()
            
        painter = QtGui.QPainter(self)
        for poly in self.listOfPolygon:
            painter.drawPolygon(poly)
            
    
    def draw_rect(self):
            
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
                        
                        self.listOfPolygon.append(polygon)
                    paint = not paint
                    
            self.first_time = False
        
    def draw_triangle(self):
        
        point = QtCore.QPointF(-0.5 * self.length, -TRIANGLE_CONST * self.length)
        for j in range(0,self.numberPolygonPerColumn+2):               
            
            for i in range(-1,self.numberPolygonPerLine+2):
                
                polygon = QtGui.QPolygonF()
                polygon << QtCore.QPoint(point.x(), point.y())
                polygon << QtCore.QPoint(point.x() + 0.5 * self.length, point.y() + TRIANGLE_CONST * self.length)
                polygon << QtCore.QPoint(point.x() - 0.5 * self.length, point.y() + TRIANGLE_CONST * self.length)
                
                point.setX(point.x() + self.length)
                    
                if(i == -1 and j%2==0):
                    point_mem = polygon.at(2)
                elif(i == -1 and j%2==1):
                    point_mem  = polygon.at(1)
                
                self.listOfPolygon.append(polygon)
                
            point = point_mem
        self.first_time = False
                    
    def draw_hexagon(self):
        painter = QtGui.QPainter(self)  
        
        self.first_time = False
        
    """DEBUT DE DEFORMATION NE MARCHE BIEN QU'AVEC LES TRIANGLES
    AVEC LES CARRES çA MARCHE MAIS POUR 1 TRAIT SUR 2 ET C'EST NORMAL VU QU'ON DESSIN LA MOITIE DES CARRES"""    
    def mouseReleaseEvent(self, event): # evenement mouseRelease
        if(self.point_to_add):  
            vector = (event.pos().x() - self.listOfPolygon[self.poly].at(self.indice - 1).x(), event.pos().y() - self.listOfPolygon[self.poly].at(self.indice - 1).y())  
            for j in range(0,len(self.listOfPolygon) - 1):
               point = QtCore.QPointF(vector[0] + self.listOfPolygon[j].at((self.indice - 1)).x(),vector[1] + self.listOfPolygon[j].at(self.indice - 1).y())
               self.listOfPolygon[j].insert(self.indice,point)
               
            self.update()
            self.point_to_add = False
        
       
    def mousePressEvent(self, event): # evenement mousePress
        self.pStart = event.pos()
        
        for j in range(0,len(self.listOfPolygon)):
            for i in range (0,self.listOfPolygon[j].count() + 1):
                if (self.point_to_add == False):
                   
                    
                    X = (min(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).x() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).x() + 10),
                        max(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).x() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).x() + 10))
                    Y = (min(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).y() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).y() + 10),
                        max(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).y() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).y() + 10))
                    
                    if(X[0] < self.pStart.x() < X[1] and Y[0] < self.pStart.y() < Y[1]):
                        self.indice = i + 1
                        self.poly = j
                        self.point_to_add = True
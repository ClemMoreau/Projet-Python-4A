# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:10:12 2021

@author: cleme
"""

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import math

TRIANGLE_CONST = math.sqrt(3)/2

class Contain(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None
        self.numberPolygonPerLine = 12
        self.length = 1600//self.numberPolygonPerLine
        self.numberPolygonPerColumn = 1600//self.length
        self.listOfPolygon = []
        
        self.add = False
        self.first = True
        
    def draw_triangle(self):
        if(self.first):
            point = QtCore.QPointF(-0.5 * self.length, -TRIANGLE_CONST * self.length)
            for j in range(0,self.numberPolygonPerColumn+2):               
                
                for i in range(-1,self.numberPolygonPerLine+2):
                
                    iLength = i * self.length
                    jLength = j * self.length
                    
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
            self.first = False
                    
        
    def draw_rect(self):
        if(self.first):
            #painter = QtGui.QPainter(self)
            
            for j in range(-1, (self.numberPolygonPerColumn + 1)):
                if (j % 2 == 0):
                    paint = True
                else:
                    paint = False
                        
                for i in range(-1, (self.numberPolygonPerLine + 1)):
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
                        
                        #painter.drawPolygon(polygon)
                        
                        self.listOfPolygon.append(polygon)
                    paint = not paint
                    self.first = False
        
    def paintEvent(self, event):
       self.draw_triangle()
       painter = QtGui.QPainter(self)
       for poly in self.listOfPolygon:
           painter.drawPolygon(poly)
    
    def mouseReleaseEvent(self, event): # evenement mouseRelease
        if(self.add):  
            vector = (event.pos().x() - self.listOfPolygon[self.poly].at(self.indice - 1).x(), event.pos().y() - self.listOfPolygon[self.poly].at(self.indice - 1).y())  
            for j in range(0,len(self.listOfPolygon) - 1):
               point = QtCore.QPointF(vector[0] + self.listOfPolygon[j].at((self.indice - 1)).x(),vector[1] + self.listOfPolygon[j].at(self.indice - 1).y())
               self.listOfPolygon[j].insert(self.indice,point)
               
            self.update()
            self.add = False
        
       
    def mousePressEvent(self, event): # evenement mousePress
        self.pStart = event.pos()
        
        for j in range(0,len(self.listOfPolygon)):
            for i in range (0,self.listOfPolygon[j].count() + 1):
                if (self.add == False):
                   
                    
                    X = (min(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).x() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).x() + 10),
                        max(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).x() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).x() + 10))
                    Y = (min(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).y() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).y() + 10),
                        max(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).y() - 10,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).y() + 10))
                    
                    if(X[0] < self.pStart.x() < X[1] and Y[0] < self.pStart.y() < Y[1]):
                        self.indice = i + 1
                        self.poly = j
                        self.add = True
                    
           
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
c = Contain()
MainWindow.setCentralWidget(c)
MainWindow.show()
sys.exit(app.exec_())
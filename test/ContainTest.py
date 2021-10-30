# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:10:12 2021

@author: cleme
"""

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import math

class Contain(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None
        self.numberPolygonPerLine = 52
        self.length = 1600//self.numberPolygonPerLine
        self.numberPolygonPerColumn = 1600//self.length
        self.listOfPolygon = []
        self.add = False
        self.first = True
        
    def draw_rect(self):
        if(self.first):
            #painter = QtGui.QPainter(self)
            
            for i in range(-1, (self.numberPolygonPerLine + 2)):
            
                
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
                        
                        #painter.drawPolygon(polygon)
                        
                        self.listOfPolygon.append(polygon)
                    paint = not paint
                    self.first = False
        
    def paintEvent(self, event):
       self.draw_rect()
       painter = QtGui.QPainter(self)
       for poly in self.listOfPolygon:
           painter.drawPolygon(poly)
    
    def mouseReleaseEvent(self, event): # evenement mouseRelease
        if(self.add):  
            
            
            self.listOfPolygon[self.poly].insert(self.indice,event.pos())
            for i in range (0,self.listOfPolygon[self.poly].count()):
                print(i ," ", self.listOfPolygon[self.poly].at(i))
            self.update()
            self.add = False
        
       
    def mousePressEvent(self, event): # evenement mousePress
        self.pStart = event.pos()
        print("press: ", self.pStart) 
        
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
                        print("depuis press ",i)
                        self.add = True
                    
           
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
c = Contain()
MainWindow.setCentralWidget(c)
MainWindow.show()
sys.exit(app.exec_())
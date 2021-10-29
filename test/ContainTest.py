# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:10:12 2021

@author: cleme
"""

from PyQt5 import QtWidgets, QtGui, QtCore, Qt

class Contain(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None
        rect = QtGui.QPolygonF()
        rect << QtCore.QPoint(10,100)
        print(rect.at(0))
        rect << QtCore.QPoint(200,100)
        print(rect.at(1))
        rect << QtCore.QPoint(200,200)
        print(rect.at(2))
        rect << QtCore.QPoint(10,200)
        print(rect.at(3))
        self.poly = rect
        self.add = False
        
        
    def mouseMoveEvent(self, event): # evenement mouseMove
        self.cursorPos = event.pos()    # on stocke la position du curseur

    def paintEvent(self, event):
       painter = QtGui.QPainter(self)
       
       painter.drawPolygon(self.poly)
    
    def mouseReleaseEvent(self, event): # evenement mouseRelease
        if(self.add):
            self.pEnd = event.pos()
            print(self.indice)
            self.poly.insert(self.indice+1,self.pEnd)
            self.update()
            self.add = False
        
       
    def mousePressEvent(self, event): # evenement mousePress
        self.pStart = event.pos()
        print("press: ", self.pStart) 
        poly =QtGui.QPolygonF()
        poly << self.pStart
        if (self.poly.intersects(poly)):
            for i in range(0,self.poly.count()):
                if(self.poly.at(i).x() - 5 < self.pStart.x() < self.poly.at(i+1).x() + 5 and
                   self.poly.at(i).y() - 5 < self.pStart.y() < self.poly.at(i+1).y() + 5):
                    print("in")
                    self.add = True
                    self.indice = i
                    print(i)
           
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
c = Contain()
MainWindow.setCentralWidget(c)
MainWindow.show()
sys.exit(app.exec_())
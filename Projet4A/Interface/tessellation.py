# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:22:13 2021

@author: cleme
"""
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore


class Tessellation(QtWidgets.QWidget):
    
    def __init__(self, polygon):
        super().__init__()
        
        self.polygon = polygon
        
        self.coordinateOfPolygon = [[None for j in range(polygon.size[1] + 1)] for i in range(polygon.get_nb_poly_per_line() + 1)]
        self.typeofPolygon = type(polygon)
        
        self.listOfPolygon = self.polygon.generate_poly()    
            
        self.point_to_add = False
       
    #evenement QPaintEvent
    def paintEvent(self, event):   # event de type QPaintEvent
        # recupere le QPainter du widget
        painter = QtGui.QPainter(self)
        for poly in self.listOfPolygon:
            painter.drawPolygon(poly)
    
        
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
            for i in range (0,self.listOfPolygon[j].count()):
                    
                    """Remplacer par un truc qui vérifie juste si projection est dans le segment"""
                    #get the x coordinate of the i and i+1 point in the j polygon
                    X = (min(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).x() - 0,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).x() + 0),
                        max(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).x() - 0,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).x() + 0))
                    
                    #get the y coordinate of the i and i+1 point in the j polygon
                    Y = (min(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).y() - 0,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).y() + 0),
                        max(self.listOfPolygon[j].at(i % self.listOfPolygon[j].count()).y() - 0,self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).y() + 0))
                    
                    if(X[0] - 5 < self.pStart.x() < X[1] + 5 and Y[0] - 5 < self.pStart.y() < Y[1] + 5):
                        
                         V = np.array([self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).x() - self.listOfPolygon[j].at((i)% self.listOfPolygon[j].count()).x(),self.listOfPolygon[j].at((i+1)% self.listOfPolygon[j].count()).y() - self.listOfPolygon[j].at((i)% self.listOfPolygon[j].count()).y()])
                         U = np.array([self.pStart.x() - self.listOfPolygon[j].at((i)% self.listOfPolygon[j].count()).x(), self.pStart.y() - self.listOfPolygon[j].at((i)% self.listOfPolygon[j].count()).y()])
                        
                         proj = (np.dot(U, V)/np.dot(V, V))*V

                         #3 is the margin
                         if (all((U-proj) <= 2) and
                             all((U-proj) >= -2)):
                             self.indice = i + 1
                             self.poly = j
                             self.point_to_add = True           

        
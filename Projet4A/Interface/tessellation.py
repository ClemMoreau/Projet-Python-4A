# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:22:13 2021

@author: cleme
"""
import math, numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore

TRIANGLE_CONST = math.sqrt(3)/2


class Tessellation(QtWidgets.QWidget):
    
    def __init__(self,size,numberPolygonPerLine, typeofPolygon):
        super().__init__()
        
        self.size = size
        
        self.numberPolygonPerLine = numberPolygonPerLine
        self.length = self.size[0]/self.numberPolygonPerLine
        self.numberPolygonPerColumn = round((self.numberPolygonPerLine*self.size[1])/self.size[0])
        print(self.numberPolygonPerColumn)
        
        self.coordinateOfPolygon = [[None for j in range(size[1] + 1)] for i in range(size[0] + 1)] #divide in coulumn
        #self.coordinateOfPolygon = [[None for j in range(size[0] + 1)] for i in range(size[1] + 1)] #divide in lines
        self.typeofPolygon = typeofPolygon
        self.listOfPolygon = []        
        
        if (self.typeofPolygon == "Square"):
            self.draw_rect()  
        if (self.typeofPolygon == "Triangle"):
            self.draw_triangle()
        if (self.typeofPolygon == "Hexagon"):
            self.draw_hexagon()
            
        self.point_to_add = False
      
    #evenement QPaintEvent
    def paintEvent(self, event):   # event de type QPaintEvent
     
        # recupere le QPainter du widget
        painter = QtGui.QPainter(self)
        for poly in self.listOfPolygon:
            painter.drawPolygon(poly)
            
    
    def draw_rect(self):
            
            for i in range(-1, (self.numberPolygonPerColumn + 1)):
                
                #boolean used to drawn on in two squares
                if (i % 2 == 0):
                    paint = True
                else:
                    paint = False
                    
                for j in range(-1, (self.numberPolygonPerLine + 1)):
                    
                    if(paint):
                        #new polygon in the tessellation
                        polygon = QtGui.QPolygonF()
                        
                        abscissa = (j * self.length)
                        ordinate = (i * self.length)
                        
                        #Top-Left point
                        polygon << QtCore.QPointF(abscissa, ordinate)
                        #Top-Right point
                        polygon << QtCore.QPointF(self.length + abscissa, ordinate)
                        #Bot-right point
                        polygon << QtCore.QPointF(self.length + abscissa, self.length + ordinate)
                        #Bot-left point
                        polygon << QtCore.QPointF(abscissa, self.length + ordinate)
                        
                        self.listOfPolygon.append(polygon)
                        #pour éviter de dépasser de la liste, de toute façon on ne peux cliquer que sur l'écran
                        if(0 <= int(polygon.at(0).x()) <= self.size[0] and 
                           0 <= int(polygon.at(0).y()) <= self.size[1]):
                            self.coordinateOfPolygon[int(polygon.at(0).x())][int(polygon.at(0).y())] = polygon
                        
                    paint = not paint
        
    def draw_triangle(self):
        
        point = QtCore.QPointF(-0.5 * self.length, -TRIANGLE_CONST * self.length)
        for j in range(0,self.numberPolygonPerColumn + 2):               
            
            #end at numberPolygonPerLine + 2 to exceeds the screen
            for i in range(0,self.numberPolygonPerLine + 2):
                
                polygon = QtGui.QPolygonF()
                polygon << QtCore.QPoint(point.x(), point.y())
                polygon << QtCore.QPoint(point.x() + 0.5 * self.length, point.y() + TRIANGLE_CONST * self.length)
                polygon << QtCore.QPoint(point.x() - 0.5 * self.length, point.y() + TRIANGLE_CONST * self.length)
                
                point.setX(point.x() + self.length)
                    
                if(i == 0 and j%2==0):
                    point_mem = polygon.at(2)
                elif(i == 0 and j%2==1):
                    point_mem  = polygon.at(1)
                
                self.listOfPolygon.append(polygon) 
                #pour éviter de dépasser de la liste, de toute façon on ne peux cliquer que sur l'écran
                if(0 <= int(polygon.at(0).x()) <= self.size[0] and 
                   0 <= int(polygon.at(0).y()) <= self.size[1]):
                    self.coordinateOfPolygon[int(polygon.at(0).x())][int(polygon.at(0).y())] = polygon
                    
            point = point_mem
                    
    def draw_hexagon(self):
        for j in range(0,self.numberPolygonPerColumn+2):               
            
            for i in range(-1,self.numberPolygonPerLine+2):
                
                polygon = QtGui.QPolygonF()
        
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
        print(self.pStart)
        
        """for j in range(0,len(self.listOfPolygon)):
            
            for i in range (0,self.listOfPolygon[j].count()):
                    
                    #Remplacer par un truc qui vérifie juste si projection est dans le segment
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
            """
        for i in range(-1,2):
            liste = self.coordinateOfPolygon[int(event.pos().x())+i]
            print(liste)
            for poly in liste:
                if(poly != None):
                    for j in range(0,poly.count()):
                        
                        vector = np.array([poly.at((j+1) % poly.count()).x() - poly.at(j % poly.count()).x(), poly.at((j+1) % poly.count()).y() - poly.at(j % poly.count()).y()])
                        vectorNewPoint = np.array([event.pos().x() - poly.at(j % poly.count()).x(),event.pos().y() - poly.at(j% poly.count()).y()])
                        
                        #calculate projection of vectorNewPoint on vector
                        vectorProjection = (np.dot(vectorNewPoint, vector)/np.dot(vector,vector))*vector
                        normeVector = math.sqrt(math.pow(vectorProjection[0],2)+math.pow(vectorProjection[1],2))
                        print(normeVector)
                        if (normeVector <= 10):
                            print("yes")
                            X = (min(poly.at((j+1) % poly.count()).x(),poly.at((j) % poly.count()).x()),
                                 max(poly.at((j+1) % poly.count()).x(),poly.at((j) % poly.count()).x()))
                            
                            #get the y coordinate of the i and i+1 point in the j polygon
                            Y = (min(poly.at((j+1) % poly.count()).y(),poly.at((j) % poly.count()).y()),
                                 max(poly.at((j+1) % poly.count()).y(),poly.at((j) % poly.count()).y()))
                            
                            if (X[0] <= vectorProjection[0] <= X[1] and
                                Y[0] <= vectorProjection[0] <= Y[1]):
                                self.indice = j + 1
                                self.poly = self.listOfPolygon.index(poly)
                                self.point_to_add = True   
                
                    
        #LE PASSEZ DANS UNE METHODE 'EST SUR SEGMENT POLYGONE' ?
    
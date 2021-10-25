# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:30:38 2021

@author: jeana
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import math



class Dessin(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setMouseTracking(False) #activer le "mouse tracking"
    
    def mouseMoveEvent(self, event): # evenement mouseMove
        self.pStart = event.pos()
        print("move: ", self.pStart)
    
    #evenement QPaintEvent
    def paintEvent(self, event):   # event de type QPaintEvent
       
        painter = QtGui.QPainter(self)             # recupere le QPainter du widget
        taille = i//nbH
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
                    #Si m est impair on  dessine des trianlge orienté vers le haut
                    polygon = QtGui.QPolygon()
                    polygon << QtCore.QPoint(0.5*taille + k*taille,0+m*taille * ((math.sqrt(3))/2))
                    polygon << QtCore.QPoint(0 + k * taille, taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2 )
                    polygon << QtCore.QPoint(taille + k * taille, taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2 )
                    painter.drawPolygon(polygon)
                
                #A chaque itération on dessine les segments qui finissent les triangles non tracés
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0,0+m*taille * ((math.sqrt(3))/2))
                polygon << QtCore.QPoint(0.5*taille,0+m*taille * ((math.sqrt(3))/2))
                painter.drawPolygon(polygon)
                
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0.5*taille + k*taille, taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2)
                polygon << QtCore.QPoint(0.5*taille + (k+1)*taille,taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2)
                painter.drawPolygon(polygon)


                #painter.drawLine(0,0+m*taille * ((math.sqrt(3))/2),0.5*taille,0+m*taille * ((math.sqrt(3))/2))
                #painter.drawLine(0.5*taille + k*taille, taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2,0.5*taille + (k+1)*taille,taille * m * ((math.sqrt(3))/2) + taille*(math.sqrt(3))/2)
                
        return
    
    def mousePressEvent(self, event): # evenement mousePress
        self.pStart = event.pos()
        print("press: ", self.pStart)

    def mouseReleaseEvent(self, event): # evenement mouseRelease
        self.pStart = event.pos()
        print("release: ", event.pos())
        
def main(args):
    global i,j 
    global nbH
    app = QtWidgets.QApplication(args)
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    j = size.height()
    i = size.width()
    nbH = 24
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))
    win = QtWidgets.QMainWindow()
    win.setCentralWidget(Dessin())
    win.resize(300,200)
    win.show()
    app.exec_()
    return

if __name__ == "__main__":
    main(sys.argv)
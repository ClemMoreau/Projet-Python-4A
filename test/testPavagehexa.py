# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:46:44 2021

@author: jeana
"""

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
                if (m%2 == 0) :
                    polygon = QtGui.QPolygon()
                    polygon << QtCore.QPoint((math.sqrt(3)/2) * taille + k * taille * math.sqrt(3),  taille * m *1.5)
                    #point haut gauche
                    polygon << QtCore.QPoint(0 + k*taille*math.sqrt(3), 0.5* taille + m  * taille * 1.5)
                    #point bas gauche 
                    polygon << QtCore.QPoint(0+ k * taille* math.sqrt(3),1.5 * taille +   taille * m *1.5  )
                    #point bas milieu
                    polygon << QtCore.QPoint((math.sqrt(3)/2) * taille + k * taille * math.sqrt(3), 2 * taille + 1.5 * taille * m)
                    #point bas droite
                    polygon << QtCore.QPoint(math.sqrt(3)*taille + math.sqrt(3)*taille * k, 1.5 * taille + 1.5 * m * taille)
                    #point haut droite
                    polygon << QtCore.QPoint(math.sqrt(3)*taille + math.sqrt(3)*taille * k, taille * 0.5 + taille * m * 1.5 )
                    painter.drawPolygon(polygon)
                    
                
            
                polygon2 = QtGui.QPolygon()
                polygon2 << QtCore.QPoint((math.sqrt(3)/2) * taille + k * taille * math.sqrt(3),taille * m * 2)
                polygon2 << QtCore.QPoint((math.sqrt(3)/2) * taille + k * taille * math.sqrt(3), 3 * taille * m)
                painter.drawPolygon(polygon2)


    
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
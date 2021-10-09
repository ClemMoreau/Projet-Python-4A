# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys



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
                #painter.drawRect(0+k*taille,0+m*taille,taille,taille)         # dessiner un rectangle noir
                
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(0+k*taille,0+m*taille)
                polygon << QtCore.QPoint(taille+k*taille,0+m*taille)
                polygon << QtCore.QPoint(taille+k*taille,taille+m*taille)
                polygon << QtCore.QPoint(0+k*taille,taille+m*taille)
                painter.drawPolygon(polygon)
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
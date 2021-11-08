# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:11:40 2021

@author: cleme
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Dessin(QWidget):

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None
        
    def mouseMoveEvent(self, event): # evenement mouseMove
        self.cursorPos = event.pos()    # on stocke la position du curseur
        self.update()    # on met à jour l'affichage7
        
    def mousePressEvent(self,event):
        print(event.pos())
    
    #evenement QPaintEvent
    def paintEvent(self, event):
        if self.cursorPos != None:
            painter = QPainter(self)
            painter.drawEllipse(\
            self.cursorPos.x()-5,\
            self.cursorPos.y()-5,10,10) # On dessine l'ellipse autour du curseur
                
def main(args):
    app = QApplication(args)
    win = QMainWindow()
    win.setCentralWidget(Dessin())
    win.resize(300,200)
    win.show()
    app.exec_()
    return

if __name__ == "__main__":
    main(sys.argv)
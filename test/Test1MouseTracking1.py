# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:11:40 2021

@author: cleme
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import Qt
import sys

class Dessin(QWidget):

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None
        
        self.poly = QPolygonF()
        self.poly << QPointF(10,10)
        self.poly << QPointF(110,10)
        self.poly << QPointF(110,110)
        self.poly << QPointF(10,110)
    
        self.marge = QPolygonF()
        self.marge << QPointF(15,15)
        self.marge << QPointF(105,15)
        self.marge << QPointF(105,105)
        self.marge << QPointF(15,105)
    
    #evenement QPaintEvent
    def paintEvent(self, event):
            painter = QPainter(self)
            painter.drawPolygon(self.poly)
            painter.setPen(QColor("green"))
            painter.drawPolygon(self.marge)
            painter.drawEllipse(\
            10-5,\
            10-5,10,10)
                
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
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:11:40 2021

@author: cleme
"""
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import sys
import pickle as pic

class Dessin(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.list = []
        
    def mouseMoveEvent(self, event): # evenement mouseMove
        self.cursorPos = event.pos()    # on stocke la position du curseur
        self.update()    # on met à jour l'affichage7
        
    def mousePressEvent(self,event):
        path = "C:/Users/cleme/OneDrive/Bureau/testPython.p"
        file = open(path,"wb")
        pic.dump(self.polygon_list,file)
        file.close()
        path = "C:/Users/cleme/OneDrive/Bureau/testPython.p"
        file = open(path,"rb")
        self.list = pic.load(file)
        file.close()
        self.update()
        
    #evenement QPaintEvent
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for poly in self.list:
            painter.drawPolygon(poly)
            
            
               
                
def main(args):
    app = QtWidgets.QApplication(args)
    win = QtWidgets.QMainWindow()
    win.setCentralWidget(Dessin())
    win.resize(300,200)
    win.show()
    app.exec_()
    return

if __name__ == "__main__":
    main(sys.argv)
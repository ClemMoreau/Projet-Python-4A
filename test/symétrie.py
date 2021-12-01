from PyQt5 import QtWidgets, QtGui, QtCore, Qt


class truc(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
    def paintEvent(self, event):
        
        painter = QtGui.QPainter(self)
        poly = QtGui.QPolygon()
        
        poly << QtCore.QPoint(100,100)
        poly << QtCore.QPoint(200,100)
        poly << QtCore.QPoint(200,200)
        poly << QtCore.QPoint(100,200)
        painter.drawPolygon(poly)
        self.mid = self.midlle(poly)
        painter.drawPoint(self.mid)
        
        point = QtCore.QPoint(250,200)
        
        poly.insert(2, point)
        painter.drawPolygon(poly)
        
        sym = self.symetrie(point)
        
        painter.drawPoint(sym)

        symint = QtCore.QPoint(sym.x(),sym.y())
        poly.insert(5, symint)
        
        painter.drawPolygon(poly)
        
    def midlle(self,poly):
        point = QtCore.QPointF()
        for i in poly:
            point += i
        point /= poly.count()
        return point
    
    def symetrie(self, point):
        vector = (self.mid.x() - point.x(),
                  self.mid.y() - point.y())
        
        sym = QtCore.QPointF(self.mid.x() + vector[0],
                             self.mid.y() + vector[1])
        return sym
        
import sys
app = QtWidgets.QApplication(sys.argv)
w = truc()
w.show()
sys.exit(app.exec_())
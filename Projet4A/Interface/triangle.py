import polygon as poly, math
from PyQt5 import QtGui, QtCore

TRIANGLE_CONST = math.sqrt(3)/2

class Triangle(poly.Polygon):
    
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
    def __init__(self, size , nb_poly_per_line):
        
        super().__init__(size, nb_poly_per_line)
        
#==============================================================================    
#   METHODS
#==============================================================================
     
    def generate_poly(self):
            
        polygon_list = []
        
        point = QtCore.QPointF(-0.5 * self.length, -TRIANGLE_CONST * self.length)
        for j in range(0,self.nb_poly_per_column + 2):               
            
            #end at numberPolygonPerLine + 2 to exceeds the screen
            for i in range(0,self.nb_poly_per_line + 2):
                
                polygon = QtGui.QPolygonF()
                polygon << QtCore.QPoint(point.x(), point.y())
                polygon << QtCore.QPoint(point.x() + 0.5 * self.length, point.y() + TRIANGLE_CONST * self.length)
                polygon << QtCore.QPoint(point.x() - 0.5 * self.length, point.y() + TRIANGLE_CONST * self.length)
                
                point.setX(point.x() + self.length)
                    
                if(i == 0 and j%2==0):
                    point_mem = polygon.at(2)
                elif(i == 0 and j%2==1):
                    point_mem  = polygon.at(1)
                
                polygon_list.append(polygon) 
                #pour éviter de dépasser de la liste, de toute façon on ne peux cliquer que sur l'écran
                """if(0 <= int(polygon.at(0).x()) <= self.size[0] and 
                   0 <= int(polygon.at(0).y()) <= self.size[1]):
                    self.coordinateOfPolygon[int(polygon.at(0).x())][int(polygon.at(0).y())] = polygon
                """
            point = point_mem
        return polygon_list
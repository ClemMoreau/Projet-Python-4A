import polygon as poly, math
from PyQt5 import QtGui, QtCore

#déplacer à l'intérieur de la classe?
TRIANGLE_CONST = math.sqrt(3)/2

class Triangle(poly.Polygon):
    
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
    def __init__(self, size , nb_poly_per_line):
        
        super().__init__(size, nb_poly_per_line)
        self.nb_poly_per_column = round((size[1]//(self.length * TRIANGLE_CONST)))

#==============================================================================    
#   GETTERS
#==============================================================================

    def get_nb_poly_per_column(self):
        return self.nb_poly_per_column 
    
#==============================================================================    
#   SETTERS
#==============================================================================

    def set_nb_poly_per_column(self, nb):
        if(nb > 0):
            self.nb_poly_per_column = nb
            
#==============================================================================    
#   METHODS
#==============================================================================
     
    def generate_poly(self):
            
        polygon_list = []
        
        point = QtCore.QPointF(-0.5 * self.length, -TRIANGLE_CONST * self.length)
        for j in range(0,self.nb_poly_per_column + 1):               
            
            #end at numberPolygonPerLine + 2 to exceeds the screen
            for i in range(0,self.nb_poly_per_line + 2):
                
                polygon = QtGui.QPolygon()
                polygon << QtCore.QPoint(point.x(), point.y())
                polygon << QtCore.QPoint(point.x() + 0.5 * self.length, 
                                         point.y() + TRIANGLE_CONST * self.length)
                polygon << QtCore.QPoint(point.x() - 0.5 * self.length,
                                         point.y() + TRIANGLE_CONST * self.length)
                
                point.setX(point.x() + self.length)
                    
                if(i == 0 and j%2==0):
                    point_mem = polygon.at(2)
                elif(i == 0 and j%2==1):
                    point_mem  = polygon.at(1)
                
                polygon_list.append(polygon) 
                
            point = point_mem
        return polygon_list
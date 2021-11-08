import polygon as poly
from PyQt5 import QtGui, QtCore

class Square(poly.Polygon):
    
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
        for i in range(-1, (self.nb_poly_per_column + 1)):
            
            #boolean used to drawn on in two squares
            if (i % 2 == 0):
                paint = True
            else:
                paint = False
                
            for j in range(-1, (self.nb_poly_per_line + 1)):
                
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
                    
                    polygon_list.append(polygon)
                    #pour éviter de dépasser de la liste, de toute façon on ne peux cliquer que sur l'écran
                    """if(0 <= int(polygon.at(0).x()) <= self.size[0] and 
                       0 <= int(polygon.at(0).y()) <= self.size[1]):
                        self.coordinateOfPolygon[int(polygon.at(0).x())][int(polygon.at(0).y())] = polygon"""
                    
                paint = not paint
        return polygon_list
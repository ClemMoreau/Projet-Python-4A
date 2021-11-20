import polygon as poly, math
from PyQt5 import QtGui, QtCore

TRIANGLE_CONST = math.sqrt(3)/2
HEXAGON_CONST = math.sqrt(3)

class Hexagon(poly.Polygon):
    
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
    def __init__(self, size , nb_poly_per_line):
        
        super().__init__(size, nb_poly_per_line)
        self.nb_poly_per_column = round((size[1]//self.length))

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
        for i in range(-1, (self.nb_poly_per_column + 1)):
            
            #boolean used to drawn on in two squares
            if (i % 2 == 0):
                paint = True
            else:
                paint = False
                
            for j in range(-1, (self.nb_poly_per_line + 1)):
                
                if(paint):
                    #new polygon in the tessellation
                    polygon = QtGui.QPolygon()
                    
                    
                if (j%2 == 0) :
                    polygon = QtGui.QPolygon()
                    polygon << QtCore.QPoint((TRIANGLE_CONST) * self.length + i * self.length * math.sqrt(3),  self.length * j *1.5)
                    #point haut gauche
                    polygon << QtCore.QPoint(0 + i*self.length*math.sqrt(3), 0.5* self.length + j  * self.length * 1.5)
                    #point bas gauche 
                    polygon << QtCore.QPoint(0+ i * self.length* math.sqrt(3),1.5 * self.length +   self.length * j *1.5  )
                    #point bas milieu
                    polygon << QtCore.QPoint((TRIANGLE_CONST) * self.length + i * self.length * math.sqrt(3), 2 * self.length + 1.5 * self.length * j)
                    #point bas droite
                    polygon << QtCore.QPoint(math.sqrt(3)*self.length + HEXAGON_CONST*self.length * i, 1.5 * self.length + 1.5 * j * self.length)
                    #point haut droite
                    polygon << QtCore.QPoint(math.sqrt(3)*self.length + HEXAGON_CONST*self.length * i, self.length * 0.5 + self.length * j * 1.5 )
                    polygon_list.append(polygon)            
                    
            
                #polygon2 = QtGui.QPolygon()
                #polygon2 << QtCore.QPoint((TRIANGLE_CONST) * self.length + i * self.length * HEXAGON_CONST,self.length * j * 2)
                #polygon2 << QtCore.QPoint((TRIANGLE_CONST) * self.length + i * self.length * HEXAGON_CONST, 3 * self.length * j)
                #polygon_list.append(polygon2)

        return polygon_list
from model.polygon import Polygon
from PyQt5 import QtGui, QtCore
import math

TRIANGLE_CONST = math.sqrt(3)/2
HEXAGON_CONST = math.sqrt(3)

class Hexagon(Polygon):
    
    #==========================================================================
    #   CONSTRUCTOR
    #==========================================================================
    def __init__(self, size , nb_poly_per_line):
        
        super().__init__(size, nb_poly_per_line)
        
        self.nb_poly_per_column = round((size[1]//self.length))
        
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
                    
                    
                if (j%2 == 0) :
                    polygon = QtGui.QPolygonF()
                    #haut milieu
                    polygon << QtCore.QPointF((TRIANGLE_CONST) * self.length + i * self.length * HEXAGON_CONST,  self.length * j *1.5)
                    #point haut gauche
                    polygon << QtCore.QPointF(0 + i*self.length*HEXAGON_CONST, 0.5* self.length + j  * self.length * 1.5)
                    #point bas gauche 
                    polygon << QtCore.QPointF(0+ i * self.length* HEXAGON_CONST,1.5 * self.length +   self.length * j *1.5  )
                    #point bas milieu
                    polygon << QtCore.QPointF((TRIANGLE_CONST) * self.length + i * self.length * HEXAGON_CONST, 2 * self.length + 1.5 * self.length * j)
                    #point bas droite
                    polygon << QtCore.QPointF(math.sqrt(3)*self.length + HEXAGON_CONST*self.length * i, 1.5 * self.length + 1.5 * j * self.length)
                    #point haut droite
                    polygon << QtCore.QPointF(math.sqrt(3)*self.length + HEXAGON_CONST*self.length * i, self.length * 0.5 + self.length * j * 1.5 )
                    polygon_list.append(polygon)            
                    
                    polygon2 = QtGui.QPolygonF()
                    #haut milieu
                    polygon2 << QtCore.QPointF(0+ i * self.length* HEXAGON_CONST,1.5 * self.length +   self.length * j *1.5)
                    #haut gauche 
                    polygon2 << QtCore.QPointF((i * self.length* HEXAGON_CONST) - HEXAGON_CONST * self.length * 0.5 , 2 * self.length +   self.length * j *1.5)                    
                    #bas gauche
                    polygon2 << QtCore.QPointF((i * self.length* HEXAGON_CONST) - HEXAGON_CONST *self.length* 0.5 , 3 * self.length +   self.length * j *1.5)                    
                    
                    #bas milieu 
                    polygon2 << QtCore.QPointF(0 + i*self.length*HEXAGON_CONST, 3.5* self.length + j  * self.length * 1.5)
                    #bas droite 
                    polygon2 << QtCore.QPointF((TRIANGLE_CONST) * self.length + i * self.length * HEXAGON_CONST, self.length * j *1.5 + 3*self.length)
                    
                    #haut droite 
                    polygon2 << QtCore.QPointF((TRIANGLE_CONST) * self.length + i * self.length * HEXAGON_CONST, self.length * j *1.5 + 2*self.length)
                    
                    polygon_list.append(polygon2)

        return polygon_list
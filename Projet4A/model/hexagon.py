from model.polygon import Polygon
from PyQt5 import QtGui, QtCore
import math

TRIANGLE_CONST = math.sqrt(3)/2
HEXAGON_CONST = math.sqrt(3)

class Hexagon(Polygon):
    """
    Attributes
    ----------
    nb_poly_per_column : int
        number of polygon per column on the screen
    
    Methods
    ---------------
    generate_poly()
       This methods create hexagon to show on the tesselation
    """
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    def __init__(self, size , nb_poly_per_line):
        """
        
        Initialize all the necessary attributes for the triangle object.

        Parameters
        ----------
        size : TYPE
            DESCRIPTION.
        nb_poly_per_line : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(size, nb_poly_per_line)
        
        self.nb_poly_per_column = round((size[1]//self.length))
        
            
    # =========== #
    #   GETTERS   #
    # =========== #

    def get_nb_poly_per_column(self):
        """
        Getter of the nb_poly_per_column attribute
        
        Returns
        -------
        self.nb_poly_per_column
        """
        
        return self.nb_poly_per_column 
    
    # =========== #
    #   SETTERS   #
    # =========== #
    
    def set_nb_poly_per_column(self, nb):
        """
        Setter of the nb_poly_per_column attribute
        
        Parameters
        ----------
        nb : int
            new number of polygon per line.

        Returns
        -------
        None.
        """
        
        if(nb > 0):
            
            self.nb_poly_per_column = nb
            
    # =========== #
    #   METHODS   #
    # =========== #
        
    def generate_poly(self):
        """
        Method which create hexagons using object's attribute

        Returns
        -------
        polygon_list : list<Hexagon>
            the list of generated hexagons.

        """
        
        polygon_list = []
        for i in range(-2, (self.nb_poly_per_column + 1)):
            
            #boolean used to drawn on in two squares
            if (i % 2 == 0):
                paint = True
            else:
                paint = False
                
            for j in range(-2, (self.nb_poly_per_line + 1)):
                
                abscissa = (j * self.length)
                ordinate = (i * self.length)
                
                if(paint):
                    #new polygon in the tessellation
                    polygon = QtGui.QPolygon()
                    
                    
                if (j%2 == 0) :
                    polygon = QtGui.QPolygon()
                    #haut milieu
                    polygon << QtCore.QPoint((TRIANGLE_CONST) * self.length + ordinate * HEXAGON_CONST,  abscissa * 1.5)
                    #point haut gauche
                    polygon << QtCore.QPoint(ordinate * HEXAGON_CONST, 0.5* self.length + abscissa * 1.5)
                    #point bas gauche 
                    polygon << QtCore.QPoint(ordinate * HEXAGON_CONST, 1.5 * (self.length +   abscissa))
                    #point bas milieu
                    polygon << QtCore.QPoint((TRIANGLE_CONST) * self.length + ordinate * HEXAGON_CONST, 2 * self.length + 1.5 * abscissa)
                    #point bas droite
                    polygon << QtCore.QPoint(HEXAGON_CONST * self.length + HEXAGON_CONST * ordinate, 1.5 * (self.length + abscissa))
                    #point haut droite
                    polygon << QtCore.QPoint(HEXAGON_CONST * self.length + HEXAGON_CONST * ordinate, self.length * 0.5 + abscissa * 1.5 )
                    polygon_list.append(polygon)            
                    
                    polygon2 = QtGui.QPolygon()
                    #haut milieu
                    polygon2 << QtCore.QPoint(ordinate * HEXAGON_CONST, 1.5 * (self.length + abscissa))
                    #haut gauche 
                    polygon2 << QtCore.QPoint((ordinate* HEXAGON_CONST) - HEXAGON_CONST * self.length * 0.5 , 2 * self.length +   abscissa * 1.5)                    
                    #bas gauche
                    polygon2 << QtCore.QPoint((ordinate* HEXAGON_CONST) - HEXAGON_CONST *self.length * 0.5 , 3 * self.length +   abscissa * 1.5)                    
                    
                    #bas milieu 
                    polygon2 << QtCore.QPoint(ordinate * HEXAGON_CONST, 3.5 * self.length + abscissa * 1.5)
                    #bas droite 
                    polygon2 << QtCore.QPoint(TRIANGLE_CONST * self.length + ordinate * HEXAGON_CONST, abscissa * 1.5 + 3 * self.length)
                    
                    #haut droite 
                    polygon2 << QtCore.QPoint(TRIANGLE_CONST * self.length + ordinate * HEXAGON_CONST, abscissa * 1.5 + 2 * self.length)
                    
                    polygon_list.append(polygon2)

        return polygon_list
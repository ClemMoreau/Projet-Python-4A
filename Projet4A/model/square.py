from model.polygon import Polygon
from PyQt5 import QtGui, QtCore

class Square(Polygon):
    """
    Class which generate a square
    
    Methods
    ---------------
    
    generate_poly()
        This methods create square
        The number of polygon per column 
        is calculate with the size of of 1 
        segment of the triangle and the height 
        of the triangle.
    """
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
    def __init__(self, size , nb_poly_per_line):
        """
        Parameters
        ---------------
        size : int 
            the height of the screen
            
        nb_poly_per_line : int 
            number of polygon per line (default is 5)
        """
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
        """
        Generate squares and add them to the 
        polygon_list
        """
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
                    
                    abscissa = (j * self.length)
                    ordinate = (i * self.length)
                    
                    #Top-Left point
                    polygon << QtCore.QPoint(abscissa, ordinate)
                    #Top-Right point
                    polygon << QtCore.QPoint(self.length + abscissa, ordinate)
                    #Bot-right point
                    polygon << QtCore.QPoint(self.length + abscissa, self.length + ordinate)
                    #Bot-left point
                    polygon << QtCore.QPoint(abscissa, self.length + ordinate)
                    
                    polygon_list.append(polygon)
                    
                    
                paint = not paint
        return polygon_list

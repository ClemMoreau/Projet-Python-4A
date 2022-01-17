from model.polygon import Polygon
from PyQt5 import QtGui, QtCore


class Square(Polygon):
    """
    Class which represent squares
    
    Attributes
    ----------
    nb_poly_per_column : int
        number of polygon per column on the screen
    
    Methods
    ---------------
    generate_poly()
        This methods create squares to show on the tesselation
    """
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    
    def __init__(self, size , nb_poly_per_line):
        """
        
        Initialize all the necessary attributes for the square object.
        
        Parameters
        ---------------
        size : int 
            the height of the screen
            
        nb_poly_per_line : int 
            number of polygon per line (default is 5)
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
        
        Generate a list of squares with object's attribut

        Returns
        -------
        polygon_list : list<QPolygon>
        generated list of square.

        """
        polygon_list = []
        for i in range(-1, (self.nb_poly_per_column + 1)):
            
            # Boolean used to drawn on in two squares
            if (i % 2 == 0):
                paint = True
                
            else:
                paint = False
                
            for j in range(-1, (self.nb_poly_per_line + 1)):
                
                if(paint):
                    
                    # New square in the tessellation
                    square = QtGui.QPolygon()
                    
                    abscissa = (j * self.length)
                    ordinate = (i * self.length)
                    
                    # Top-Left point
                    square << QtCore.QPoint(abscissa, 
                                            ordinate)
                    # Top-Right point
                    square << QtCore.QPoint(self.length + abscissa, 
                                            ordinate)
                    # Bot-right point
                    square << QtCore.QPoint(self.length + abscissa, 
                                            self.length + ordinate)
                    # Bot-left point
                    square << QtCore.QPoint(abscissa, 
                                            self.length + ordinate)
                    
                    polygon_list.append(square)
                    
                paint = not paint
                
        return polygon_list
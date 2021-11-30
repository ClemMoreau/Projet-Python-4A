

class Polygon:
    """
    Class which initialize parameter for 
    the square, triangle, hexagon classes
    
    Methods
    ---------------
    
    generate_poly()
        
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
        self.size = size

        self.nb_poly_per_line = nb_poly_per_line

        self.length = self.size[0]/self.nb_poly_per_line

#==============================================================================    
#   GETTERS
#==============================================================================

    def get_size(self):
        return self.size
    
    def get_length(self):
        return self.length

    def get_nb_poly_per_line(self):
        return self.nb_poly_per_line

#==============================================================================    
#   SETTERS
#==============================================================================
    def set_size(self, size):
        if(size[0] >= 0 and size[1] >= 0):
            self.size = size
            self.length = self.size[0]/self.nb_poly_per_line
            
    def set_length(self, length):
        if(length >= 0):
            self.length = length
            self.nb_poly_per_line = self.size[0]//self.length

    def set_nb_poly_per_line(self, nb):
        if(nb > 0):
            self.nb_poly_per_line = nb
            self.length = self.size[0]/self.nb_poly_per_line

#==============================================================================    
#   METHODS
#==============================================================================

    def generate_poly(self):
        pass

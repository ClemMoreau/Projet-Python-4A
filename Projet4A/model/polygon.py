

class Polygon:
    """
    
    Class which represent polygon, 
    itinitialize parameter for 
    the square, triangle, hexagon classes
    
    
    Attributes
    ----------
    size : tuple<int>
        tuple of the screen size
    nb_poly_per_line : int
        number of polygon per line on the screen
    length : float
        length of the polygon side
    
    Methods
    ---------------
    
    generate_poly()
        
    """
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
    def __init__(self, size , nb_poly_per_line):
        """
        
        Initialize all the necessary attributes for the polygon object.
        
        Parameters
        ---------------
        size : int 
            the height of the screen
            
        nb_poly_per_line : int 
            number of polygon per line (default is 5)
            
        length : float
            length of the polygon side
        """
        
        self.size = size

        self.nb_poly_per_line = nb_poly_per_line

        self.length = self.size[0]/self.nb_poly_per_line

#==============================================================================    
#   GETTERS
#==============================================================================

    def get_size(self):
        """
        Getter for the size attribute

        Returns
        -------
        self.size : tuple<int>
        """
        
        return self.size
    
    def get_length(self):
        """
        Getter for the length attribute
        
        Returns
        -------
        self.length : float
        """
        
        return self.length

    def get_nb_poly_per_line(self):
        """
        Getter for the nb_poly_per_line attribute
        
        Returns
        -------
        self.nb_poly_per_line : int
        """
        
        return self.nb_poly_per_line

#==============================================================================    
#   SETTERS
#==============================================================================
    def set_size(self, size):
        """
        Setter for the size attribute
        
        Parameters
        ----------
        size : tuple<int>
            new size for the height of the screen.

        Returns
        -------
        None.

        """
        
        if(size[0] >= 0 and size[1] >= 0):
            
            self.size = size
            self.length = self.size[0]/self.nb_poly_per_line
            
    def set_length(self, length):
        """
        Setter for the size length attribute

        Parameters
        ----------
        length : float
            new size of the polygon side.

        Returns
        -------
        None.

        """
        
        if(length >= 0):
            
            self.length = length
            self.nb_poly_per_line = self.size[0]//self.length

    def set_nb_poly_per_line(self, nb):
        """
        Setter for the size nb_poly_per_line attribute
        Parameters
        ----------
        nb : int
            new number of polygon per line.

        Returns
        -------
        None.

        """
        
        if(nb > 0):
            
            self.nb_poly_per_line = nb
            self.length = self.size[0]/self.nb_poly_per_line

#==============================================================================    
#   METHODS
#==============================================================================

    def generate_poly(self):
        """
        Method defined in the inherited classes

        Returns
        -------
        None.

        """
        pass

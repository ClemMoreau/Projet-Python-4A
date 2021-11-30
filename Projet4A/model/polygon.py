from PyQt5 import QtWidgets, QtGui, QtCore

class Polygon:

#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
    def __init__(self, size , nb_poly_per_line):
        
        
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

    def set_length(self, length):
        if(length >= 0):
            self.length = length
    
    def set_nb_poly_per_line(self, nb):
        if(nb > 0):
            self.nb_poly_per_line = nb
            
    def set_nb_poly_per_column(self, nb):
        if(nb > 0):
            self.nb_poly_per_column = nb
        
#==============================================================================    
#   METHODS
#==============================================================================
        
    def generate_poly(self):
        pass
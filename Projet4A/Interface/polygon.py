from PyQt5 import QtWidgets, QtGui, QtCore

class Polygon:

#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
    def __init__(self, size , nb_poly_per_line):
        
        super().__init__()
        self.size = size
        
        self.nb_poly_per_line = nb_poly_per_line
        self.nb_poly_per_column = round((self.nb_poly_per_line*self.size[1])/self.size[0]) #Trouvé le bon truc

        self.length = self.size[0]/self.nb_poly_per_line
        
        self.point_to_add = False
    
#==============================================================================    
#   GETTERS
#==============================================================================

    def get_size(self):
        return self.size
    
    def get_length(self):
        return self.length

    def get_nb_poly_per_line(self):
        return self.nb_poly_per_line
    
    def get_nb_poly_per_column(self):
        return self.nb_poly_per_column
    
    def get_point_to_add(self):
        return self.point_to_add
    
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
            
    def set_point_to_add(self, boolean):
        self.point_to_add = boolean
        
#==============================================================================    
#   METHODS
#==============================================================================
            
    def mousePressEvent(self, event): # evenement mousePress
        self.pStart = event.pos()
        print(self.pStart)
        
    def generate_poly(self):
        pass
import pickle
from PyQt5 import QtWidgets, QtCore


class Loader():
    """
    Class which take a saved file 
    and reuse the data inside of it
    
    Methods 
    ---------------
    
    load_object()
         method which open a saved file
         and read the binary data inside
    
    """
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
 
    def __init__(self, file_name, path = None):
        """
        Parameters
        ---------------
        
        file_name : str
            name of the file (.txt)
        path : str
            path to the place where the file is saved
            
        """
        self.path = path
        
        self.file_name = file_name
        
        self.object_loaded = None
        
#==============================================================================    
#   GETTERS
#==============================================================================

    def get_path(self):
    
        return self.path
    
    def get_file_name(self):
    
        return self.file_name

    def get_object_loaded(self):
        
        return self.object_loaded
#==============================================================================    
#   SETTERS
#==============================================================================
    
    def set_path(self, path):
        
        self.path = path
        
    def set_file_name(self, file_name):
        
        self.file_name = file_name
 
    def set_object_loaded(self, obj):
        
        if(obj != None):
            self.object_loaded = obj
#==============================================================================    
#   METHODS
#==============================================================================
          
    def load_object(self):
        """
        method which open a saved file
        and read the binary data inside

        """
        file = open(self.path + self.file_name,"rb")
        
        self.object_loaded = pickle.load(file)
        
        file.close()
        
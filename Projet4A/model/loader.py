import pickle
from PyQt5 import QtWidgets, QtCore


class Loader():
    
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
 
    def __init__(self, file_name, path = None):
        
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
        
        file = open(self.path + self.file_name,"rb")
        
        self.object_loaded = pickle.load(file)
        
        file.close()
        
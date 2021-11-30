import pickle
from PyQt5 import QtWidgets

class Saver(QtWidgets.QWidget):
    
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
 
    def __init__(self, object_to_save, file_name, path = None):
        
        super().__init__()
        
        self.path = path
        
        self.file_name = file_name
        
        self.object_to_save = object_to_save
        
#==============================================================================    
#   GETTERS
#==============================================================================

    def get_path(self):
    
        return self.path
    
    def get_file_name(self):
    
        return self.file_name
    
    def get_object_to_save(self):
        
        return self.object_to_save

#==============================================================================    
#   SETTERS
#==============================================================================
    
    def set_path(self, path):
        
        self.path = path
        
    def set_file_name(self, file_name):
        
        self.file_name = file_name
        
    def set_object_to_save(self, obj):
        
        if(obj != None):
            self.object_to_save = obj
 
#==============================================================================    
#   METHODS
#==============================================================================

    def clear_file(self):
        
        file = open(self.path + self.file_name + '.txt','w')
        file.close()
        
    def save_object(self):
        
        #rajouter pouvoir rajouter le chemin
        
        if(self.object_to_save != None):
            
            self.clear_file()
            
            file = open(self.path + self.file_name + '.txt',"wb")
            
            pickle.dump(self.object_to_save, file)
            
            file.close()
        
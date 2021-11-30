import pickle
from PyQt5 import QtWidgets

class Saver(QtWidgets.QWidget):
    """
    Class which aim to save the deformation
    apllied to the figure
    
    Methods
    ---------------
    
    clear_file()
        method which create an empty file if 
        it doesnt exist
    save_object()
        save the object into a file
        the object is converted into binary data
    """
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
 
    def __init__(self, object_to_save, file_name, path = None):
        """
        Parameters
        ---------------
        
        object_to_save : object
            the object that the user want to save
        file_name : str
            name of the file (.txt)
        path : str
            path to the place where the file is saved
            
        """
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
        """
        Method which create an empty file if 
        it doesnt exist
        """
        file = open(self.path + self.file_name + '.txt','w')
        file.close()
        
    def save_object(self):
        
        #rajouter pouvoir rajouter le chemin
        
        if(self.object_to_save != None):
            """
            Save the object into a file
            the object is converted into binary data
            """
            self.clear_file()
            
            file = open(self.path + self.file_name + '.txt',"wb")
            
            pickle.dump(self.object_to_save, file)
            
            file.close()
        
import pickle
from PyQt5 import QtWidgets, QtCore

class Saver():
    
#==============================================================================    
#   CONSTRUCTOR
#==============================================================================
 
    def __init__(self, obj, file_name, path = None):
        
        self.path = path
        
        self.file_name = file_name
        
        self.object_to_save = obj
        
        self.set_graphic_interface()
        
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
        file = open(self.file_name,'w')
        file.close()
        
    def save_object(self):
        
        if(self.object_to_save != None):
            self.clear_file()
            file = open(self.file_name,"wb")
            #self.path +
            pickle.dump(self.object_to_save, file)
            file.close()
            
    def set_graphic_interface(self):
        self.win = QtWidgets.QMainWindow()
        
        #Text label TypeOfPoly
        label_polygon_type = QtWidgets.QLabel(self.win)
        label_polygon_type.setGeometry(QtCore.QRect(40, 20, 200, 20))
        label_polygon_type.setObjectName("label_file_name")
        label_polygon_type.setText("Please choose a filename to save your tesselation : ")
        
        
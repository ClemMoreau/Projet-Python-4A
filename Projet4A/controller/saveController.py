from PyQt5 import QtWidgets, QtCore
from model.saver import Saver
from view.tessellationWindow import TessellationWindow

class SaveController(QtWidgets.QWidget):
    
    #==========================================================================
    #   CONSTRUCTOR
    #==========================================================================

    def __init__(self):
        
        super().__init__()
        
        self.set_graphic_interface()
        
    #==========================================================================
    #   GETTERS
    #==========================================================================
    
    def get_label_no_filename(self):
        return self.label_no_filename
    
    def get_line_edit_filename(self):
        return self.line_edit_filename
    
    #==========================================================================
    #   SETTERS
    #==========================================================================
    
    def set_label_no_filename(self, label):
        if(label):
            self.label_no_filename = label
            
    def set_line_edit_filename(self, line_edit):
        if(line_edit):
            self.line_edit_filename = line_edit
            
    #==========================================================================
    #   METHODS
    #==========================================================================
        
    def set_graphic_interface(self):
        
        #Text label filename of the saved tesselation
        label_filename = QtWidgets.QLabel(self)
        label_filename.setGeometry(QtCore.QRect(20, 10, 200, 20))
        label_filename.setObjectName("label_filename")
        label_filename.setText("Please choose a filename to save : ")
        
        #Text label filename of the saved tesselation
        self.save_label = QtWidgets.QLabel(self)
        self.save_label.setGeometry(QtCore.QRect(65, 65, 200, 30))
        self.save_label.setObjectName("save_label")
        
        #line edit filename of the saved tesselation
        self.line_edit_filename = QtWidgets.QLineEdit(self)
        self.line_edit_filename.setGeometry(QtCore.QRect(20, 40, 100, 20))
        self.line_edit_filename.setObjectName("line_edit_filename ")
            
        #Pushbutton to call the click function 
        push_button_save = QtWidgets.QPushButton(self)
        push_button_save.setGeometry(QtCore.QRect(20, 65, 40, 30))
        push_button_save.setObjectName("push_button_save")
        push_button_save.setText("Save")
        push_button_save.clicked.connect(self.save)

    def save(self):
        try:
        
             if(self.line_edit_filename.text() != ''):
                 Saver(TessellationWindow.get_tessellation_widget().get_polygon_information(), 
                   self.line_edit_filename.text(), 'saves/').save_object()
                 self.save_label.setText("File saved !")  
             else:
                 self.save_label.setText("You need to write a filename !")  
        except:
            self.save_label.setText("Error during saving, no file saved.")  
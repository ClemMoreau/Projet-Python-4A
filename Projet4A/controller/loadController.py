from PyQt5 import QtWidgets, QtCore
from model.loader import Loader
from view.tessellationWindow import TessellationWindow
from view.settingsWindow import SettingsWindow

import os

class LoadController(QtWidgets.QWidget):
    
    #==========================================================================
    #   CONSTRUCTOR
    #==========================================================================
    def __init__(self):
        
        super().__init__()       
        self.set_graphic_interface()
        
    #==========================================================================
    #   METHODS
    #==========================================================================
    
    def set_graphic_interface(self):
        
        self.setFixedSize(QtCore.QSize(240, 105))
        self.setWindowTitle("Load File")
        
        #Text label filename of the saved tesselation
        self.label_filename = QtWidgets.QLabel(self)
        self.label_filename.setGeometry(QtCore.QRect(20, 10, 200, 20))
        self.label_filename.setObjectName("label_filename")
        self.label_filename.setText("Please choose a filename to load : ")
        
        #line edit filename of the saved tesselation
        self.combo_box_file_to_load = QtWidgets.QComboBox(self)
        self.combo_box_file_to_load.setGeometry(QtCore.QRect(20, 40, 100, 20))
        self.combo_box_file_to_load.setObjectName("combo_box_file_to_load")
        self.combo_box_file_to_load.addItems(os.listdir('saves/polygon list/'))
        
        self.load_label = QtWidgets.QLabel(self)
        self.load_label.setGeometry(QtCore.QRect(65, 70, 200, 20))
        self.load_label.setObjectName("load_label")
        
        #Pushbutton to call the click function 
        push_button_save = QtWidgets.QPushButton(self)
        push_button_save.setGeometry(QtCore.QRect(20, 65, 40, 30))
        push_button_save.setObjectName("push_button_load")
        push_button_save.setText("Load")
        push_button_save.clicked.connect(self.load)
        
    def load(self):
        try:
            
            if(TessellationWindow.get_tessellation_widget().get_polygon_information()):
                
                loader = Loader(self.combo_box_file_to_load.currentText(), 'saves/polygon list/');
                loader.load_object()  
                if (loader.get_object_loaded()):
                    TessellationWindow.get_tessellation_widget().get_polygon_information().set_polygon_list(loader.get_object_loaded())

                loader = Loader(self.combo_box_file_to_load.currentText(), 'saves/fixed points/');
                loader.load_object()  
                if (loader.get_object_loaded()):
                    TessellationWindow.get_tessellation_widget().get_polygon_information().set_fixed_points(loader.get_object_loaded())
                 
                TessellationWindow.get_tessellation_widget().get_polygon_information().generate_coordinates()
                TessellationWindow.get_tessellation_widget().update()
                self.load_label.setText("File loaded !")
            else:
                pass
                
        except:
            
            self.load_label.setText("Error during loading, no file loaded.")
            
    def closeEvent(self, event):
        
        SettingsWindow.get_setting_widget().close()
from PyQt5 import QtWidgets, QtCore
from model.loader import Loader
from view.tessellationWindow import TessellationWindow
from view.settingsWindow import SettingsWindow
from controller.tessellation import Tessellation

import os

class LoadController(QtWidgets.QWidget):
    """
    Class which represent the widget used to load tessellation
    
    Attributes
    ----------
    load_label : QLabel
        Label used after trying to load a tessellation.
        
    combo_box_file_to_load: QComboBox 
        Combox used to select a file to load.
    
    Methods
    ---------------
    set_graphic_interface()
        This methods initialize the widget
    load()
        This methods load a tesselation
    """
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    def __init__(self):
        
        super().__init__()       
        self.set_graphic_interface()
    
    # =========== #
    #   GETTERS   #
    # =========== #

    def get_combo_box_file_to_load(self):
        """
        Getter of the combo_box_file_to_load attribute.

        Returns
        -------
        QComboBox
            Combox used to select a file to load.

        """
        return self.combo_box_file_to_load
    
    def get_load_label(self):
        """
        Getter of the load_label attribute.

        Returns
        -------
        QLabel
            Label used after trying to load a tessellation.

        """
        return self.load_label

    # =========== #
    #   SETTERS   #
    # =========== #
        
    def set_combo_box_file_to_load(self, combo_box):
        """
        Setter of the combo_box_file_to_load attribute.

        Parameters
        ----------
        combo_box : QComboBox
            the new combox used to select a file to load.

        Returns
        -------
        None.

        """
        self.combo_box_file_to_load = combo_box
        
    def set_load_label(self, label):
        """
        Setter of the load_label attribute.

        Parameters
        ----------
        label : QLabel
            the new label used after trying to load a tessellation.

        Returns
        -------
        None.

        """
        self.load_label = label    
        
    # =========== #
    #   METHODS   #
    # =========== #
    
    def set_graphic_interface(self):
        """
        Method which initialize all the widget on the LoadController widget

        Returns
        -------
        None.

        """
        
        self.setFixedSize(QtCore.QSize(240, 105))
        self.setWindowTitle("Loading")
        
        #Text label filename of the saved tesselation
        label_filename = QtWidgets.QLabel(self)
        label_filename.setGeometry(QtCore.QRect(20, 10, 200, 20))
        label_filename.setObjectName("label_filename")
        label_filename.setText("Please choose a filename to load : ")
        
        #line edit filename of the saved tesselation
        self.combo_box_file_to_load = QtWidgets.QComboBox(self)
        self.combo_box_file_to_load.setGeometry(QtCore.QRect(20, 40, 100, 20))
        self.combo_box_file_to_load.setObjectName("combo_box_file_to_load")
        self.combo_box_file_to_load.addItems(os.listdir('saves/'))
        
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
        """
        Method which load the tessellation in the file filename of 
        the repository path

        Returns
        -------
        None.

        """
        
        try:
            if(TessellationWindow.get_tessellation_widget() == None):
                TessellationWindow.set_tessellation_widget(Tessellation('Square', 1, SettingsWindow.get_setting_widget().get_combo_box_color().currentText()))
                
            
            loader = Loader(self.combo_box_file_to_load.currentText(), 'saves/');
            loader.load_object()
            TessellationWindow.get_tessellation_widget().set_polygon_information(loader.get_object_loaded())
            TessellationWindow.get_tessellation_widget().update()
                
            SettingsWindow.close_widget()
            TessellationWindow.show_widget()
                
            self.load_label.setText("File loaded !")
                
        except:
            
            self.load_label.setText("Error during loading, no file loaded.")
            
    def closeEvent(self, event):
        
        SettingsWindow.get_setting_widget().close()
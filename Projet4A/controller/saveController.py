from PyQt5 import QtWidgets, QtCore
from model.saver import Saver
from view.tessellationWindow import TessellationWindow


class SaveController(QtWidgets.QWidget):
    """
    Class which represent the widget used to save tessellation
    
    Attributes
    ----------
    save_label : QLabel
        Label used after trying to save tessellation.
        
    line_edit_filename: QLineEdit 
        Line edit used to name the file where tessellation will be saved.
    
    Methods
    ---------------
    set_graphic_interface()
        This methods initialize the widget
    save()
        This methods save the tesselation
    """
    
    #==========================================================================
    #   CONSTRUCTOR
    #==========================================================================

    def __init__(self):
        """
        Constructor of the SaveController class,
        used to call the parent constructor and initialize all its widget.

        Returns
        -------
        None.

        """
        
        super().__init__()
        
        self.set_graphic_interface()
        
    #==========================================================================
    #   GETTERS
    #==========================================================================
    
    def get_save_label(self):
        """
        Getter of the save_label attribute.

        Returns
        -------
        QLabel
            Label used after trying to save tessellation.

        """
        return self.save_label
    
    def get_line_edit_filename(self):
        """
        Getter of the line_edit_filename attribute.

        Returns
        -------
        QLineEdit
            Line edit used to name the file where tessellation will be saved.

        """
        return self.line_edit_filename
    
    #==========================================================================
    #   SETTERS
    #==========================================================================
    
    def set_save_label(self, label):
        """
        Setter of the save_label attribute.

        Parameters
        ----------
        label : QLabel
            the new label after trying to save tessellation.

        Returns
        -------
        None.

        """
        if(label):
            self.save_label = label
            
    def set_line_edit_filename(self, line_edit):
        """
        Setter f the line_edit_filename attribute.

        Parameters
        ----------
        line_edit : QLineEdit
            the new line edit used to name the file where tessellation will be saved.

        Returns
        -------
        None.

        """
        if(line_edit):
            self.line_edit_filename = line_edit
            
    #==========================================================================
    #   METHODS
    #==========================================================================
        
    def set_graphic_interface(self):
        """
        Method which initialize all the widget on the SaveController widget

        Returns
        -------
        None.

        """
        
        self.setWindowTitle("Saving")
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
        """
        Method which save the current tessellation in the file filename of 
        the repository path

        Returns
        -------
        None.

        """
        try:
        
             if(self.line_edit_filename.text() != ''):
                 Saver(TessellationWindow.get_tessellation_widget().get_polygon_information(), 
                   self.line_edit_filename.text(), 'saves/').save_object()
                 self.save_label.setText("File saved !")  
             else:
                 self.save_label.setText("You need to write a filename !")  
        except:
            self.save_label.setText("Error during saving, no file saved.")  
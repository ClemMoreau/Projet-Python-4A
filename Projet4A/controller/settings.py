from controller.tessellation import Tessellation

from view.tessellationWindow import TessellationWindow
from view.settingsWindow import SettingsWindow
from view.loadWindow import LoadWindow

from PyQt5 import QtWidgets, QtCore

# List of the color allowed for coloring
COLOR_ALLOWED = ["white", "red", "green", "blue",
                 "black", "darkRed", "darkGreen", "darkBlue",
                 "cyan", "magenta", "yellow", "gray",
                 "darkCyan", "darkMagenta", "darkYellow", "darkGray", "lightGray",
                 'rainbow']

# List of the type of polygon allowed in the software
POLYGON_TYPE = ["Triangle", "Square", "Hexagon"]


class Settings(QtWidgets.QWidget):
    """
    
    Class which represent setting widget, 
    it's the first window to appear.
    The users can chose the type of polygon,
    the number of polygon per line on the screen,
    the color of his tesselation 
    and may choose a symmetry option
    
    Attributes
    ----------
    
    Methods
    ---------------
    set_graphic_interface():
        Method which initiate widget attribute
    button_click_action():
        Method call when the user click on the button
    """

# ==============================================================================
# CONSTRUCTOR
# ==============================================================================

    def __init__(self):
        """
        
        
        Returns
        -------
        None.

        """
        super().__init__()
        # The setting widget  
        self.set_graphic_interface()

# ==============================================================================
# GETTERS
# ==============================================================================

    def get_combo_box_polygon_type(self):
        """
        Getter of the combo_box_polygon_type attribute

        Returns
        -------
        self.combo_box_polygon_type : list<String>
            combo box containing the list of polygon allowed for the tesselation.

        """
        return self.combo_box_polygon_type
    
    def get_combo_box_color(self):
        """
        Getter of the combo_box_color attribute

        Returns
        -------
        self.combo_box_color : list<String>
            combo box containing the list of color allowed for the tesselation.

        """
        return self.combo_box_color

    def get_spin_box_number_poly_per_line(self):
        """
        Getter of the spin_box_number_poly_per_line attribute

        Returns
        -------
        self.spin_box_number_poly_per_line : int
            spin box used to chose the number of poly per line.

        """
        return self.spin_box_number_poly_per_line

# ==============================================================================
# SETTERS
# ==============================================================================

    def set_combo_box_polygon_type(self, combo_box):
        """
        Setter of the combo_box_polygon_type attribute

        Parameters
        ----------
        combo_box : QComboBox
            new combo box containing 
            the list of color allowed for the tesselation.

        Returns
        -------
        None.

        """
        
        if(combo_box):
            self.combo_box_polygon_type = combo_box

    def set_spin_box_number_poly_per_line(self, spin_box):
        """
        Setter of the spin_box_number_poly_per_line attribute

        Parameters
        ----------
        spin_box : QSpinBox
            spin box used to chose the number of poly per line.

        Returns
        -------
        None.

        """
        
        if(spin_box):
            self.spin_box_number_poly_per_line = spin_box

# ==============================================================================
# METHODS
# ==============================================================================

    def set_graphic_interface(self):
        """
        Function that initalise 
        graphic interface for the settings widget,
        in order to show it to select tesselation's options.

        Returns
        -------
        None.

        """
        
        # Used to resize the window and fixe it's size
        self.setFixedSize(QtCore.QSize(260,250))
        
        # Set the window title
        self.setWindowTitle("Settings")
        
        # Text label "type of polygon" 
        label_polygon_type = QtWidgets.QLabel(self)
        label_polygon_type.setGeometry(QtCore.QRect(40, 10, 200, 20))
        label_polygon_type.setObjectName("label_polygon_type")
        label_polygon_type.setText("Please choose a type of polygon:")

        # Combo Box containing TypeOfPoly : used to choose the polygon to draw
        self.combo_box_polygon_type = QtWidgets.QComboBox(self)
        self.combo_box_polygon_type.setGeometry(QtCore.QRect(50, 30, 160, 20))
        self.combo_box_polygon_type.setObjectName("combo_box_polygon_type")
        self.combo_box_polygon_type.addItems(POLYGON_TYPE)

        # Text label to chose number of polygon per line
        label_polygon_per_line = QtWidgets.QLabel(self)
        label_polygon_per_line.setGeometry(QtCore.QRect(20, 60, 180, 25))
        label_polygon_per_line.setObjectName("label_polygon_per_line")
        label_polygon_per_line.setText("Please choose the number of polygon per line : ")

        # Spin box to select number of polygon per line [5;+∞[
        self.spin_box_number_poly_per_line = QtWidgets.QSpinBox(self)
        self.spin_box_number_poly_per_line.setGeometry(QtCore.QRect(205, 60, 40, 20))
        self.spin_box_number_poly_per_line.setMinimum(1)
        self.spin_box_number_poly_per_line.setObjectName("spin_box_number_poly_per_line")
        
        # Text label "color of the tesselation"
        label_color = QtWidgets.QLabel(self)
        label_color.setGeometry(QtCore.QRect(40, 90, 190, 25))
        label_color.setObjectName("label_color")
        label_color.setText("Please choose the color for your draw :")
        
        # Combo Box to chose a color to draw polygon
        self.combo_box_color = QtWidgets.QComboBox(self)
        self.combo_box_color.setGeometry(QtCore.QRect(50, 115, 160, 25))
        self.combo_box_color.setObjectName("combo_box_color")
        self.combo_box_color.addItems(COLOR_ALLOWED)
        
        # Radio Button used as an option for central symmetry
        self.radio_button_central_symmetry = QtWidgets.QRadioButton("Central symmetry",self)
        self.radio_button_central_symmetry.setGeometry(QtCore.QRect(50, 140, 180, 20))
        self.radio_button_central_symmetry.setObjectName("radio_button_central_symmetry")
        
        # Radio Button used as an option for central symmetry
        self.radio_button_axial_symmetry = QtWidgets.QRadioButton("Axial symmetry",self)
        self.radio_button_axial_symmetry.setGeometry(QtCore.QRect(50, 160, 180, 20))
        self.radio_button_axial_symmetry.setObjectName("radio_button_axial_symmetry")
        
        # Pushbutton to show the drawed tesselation
        push_button_draw = QtWidgets.QPushButton("Draw !",self)
        push_button_draw.setGeometry(QtCore.QRect(90, 180, 90, 50))
        push_button_draw.setObjectName("push_button_draw")
        push_button_draw.clicked.connect(self.button_click_action)

    def button_click_action(self):
        """
        Function executed when button is clicked
        Showed the tesselation windows
        
        Returns
        -------
        None.

        """
        
        #Get information to create the tesselation
        polygon_type = self.combo_box_polygon_type.currentText() 
        nb_polygon_per_line = self.spin_box_number_poly_per_line.value()
        color = self.combo_box_color.currentText()
        central_symmetry = self.radio_button_central_symmetry.isChecked()
        axial_symetry = self.radio_button_axial_symmetry.isChecked()
        SettingsWindow.close_widget()
        
        TessellationWindow.set_tessellation_widget(Tessellation(polygon_type, nb_polygon_per_line,central_symmetry, axial_symetry, color))
        TessellationWindow.show_widget()
        
        LoadWindow.close_widget()
        LoadWindow.show_widget()
        
    def closeEvent(self, event):
        
        pass
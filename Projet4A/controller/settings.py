from controller.tessellation import Tessellation

from view.tessellationWindow import TessellationWindow
from view.settingsWindow import SettingsWindow
from view.loadWindow import LoadWindow

from PyQt5 import QtWidgets, QtCore

COLOR_ALLOWED = ["white", "red", "green", "blue",
                 "black", "darkRed", "darkGreen", "darkBlue",
                 "cyan", "magenta", "yellow", "gray",
                 "darkCyan", "darkMagenta", "darkYellow", "darkGray", "lightGray",
                 'rainbow']
POLYGON_TYPE = ["Triangle", "Square", "Hexagon"]


class Settings(QtWidgets.QWidget):

# ==============================================================================
# CONSTRUCTOR
# ==============================================================================

    def __init__(self):
        super().__init__()
        # The setting widget  
        self.set_graphic_interface()

# ==============================================================================
# GETTERS
# ==============================================================================

    def get_combo_box_polygon_type(self):
        return self.combo_box_polygon_type
    
    def get_combo_box_color(self):
        return self.combo_box_color

    def get_spin_box_number_poly_per_line(self):
        return self.spin_box_number_poly_per_line

# ==============================================================================
# SETTERS
# ==============================================================================

    def set_combo_box_polygon_type(self, combo_box):
        if(combo_box):
            self.combo_box_polygon_type = combo_box

    def set_spin_box_number_poly_per_line(self, spin_box):
        if(spin_box):
            self.spin_box_number_poly_per_line = spin_box

# ==============================================================================
# METHODS
# ==============================================================================

    def set_graphic_interface(self):

        self.setFixedSize(QtCore.QSize(260,250))
        self.setWindowTitle("Settings")
        # Text label TypeOfPoly
        label_polygon_type = QtWidgets.QLabel(self)
        label_polygon_type.setGeometry(QtCore.QRect(40, 10, 200, 20))
        label_polygon_type.setObjectName("label_polygon_type")
        label_polygon_type.setText("Please choose a type of polygon:")

        # Combo Box containing TypeOfPoly
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
        
        label_color = QtWidgets.QLabel(self)
        label_color.setGeometry(QtCore.QRect(40, 90, 190, 25))
        label_color.setObjectName("label_color")
        label_color.setText("Please choose the color for your draw :")
        
        self.combo_box_color = QtWidgets.QComboBox(self)
        self.combo_box_color.setGeometry(QtCore.QRect(50, 115, 160, 25))
        self.combo_box_color.setObjectName("combo_box_color")
        self.combo_box_color.addItems(COLOR_ALLOWED)
        
        self.radio_button_central_symmetry = QtWidgets.QRadioButton("Central symmetry",self)
        self.radio_button_central_symmetry.setGeometry(QtCore.QRect(50, 140, 180, 20))
        self.radio_button_central_symmetry.setObjectName("radio_button_central_symmetry")
        
        # Pushbutton to call the click function 
        push_button_draw = QtWidgets.QPushButton("Draw !",self)
        push_button_draw.setGeometry(QtCore.QRect(90, 160, 90, 50))
        push_button_draw.setObjectName("push_button_draw")
        push_button_draw.clicked.connect(self.button_click_action)

    def button_click_action(self):

        polygon_type = self.combo_box_polygon_type.currentText() 
        nb_polygon_per_line = self.spin_box_number_poly_per_line.value()
        color = self.combo_box_color.currentText()
        central_symmetry = self.radio_button_central_symmetry.isChecked()
        
        SettingsWindow.close_widget()
        
        TessellationWindow.set_tessellation_widget(Tessellation(polygon_type, nb_polygon_per_line,central_symmetry, color))
        TessellationWindow.show_widget()
        
        LoadWindow.close_widget()
        LoadWindow.show_widget()
        
    def closeEvent(self, event):
        pass
        #LoadWindow.load_widget.close()
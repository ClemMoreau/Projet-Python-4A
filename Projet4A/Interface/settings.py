import tessellation as tess, square as sq, triangle as tri, hexagon as hexa
from PyQt5 import QtWidgets, QtCore

class settings(object):
    
#==============================================================================    
#   CONSTRUCTOR
#============================================================================== 
    
    #Changer size (tuple) en deux int ?
    def __init__(self, size):
        #The setting widget
        self.set_graphic_interface()

        #Size for the calcul of polygon length
        self.widget_max_size = size
        
#==============================================================================    
#   GETTERS
#==============================================================================
    
    def get_widget(self):
        return self.widget
    
    def get_mainWindow(self):
        return self.main_window
    
    def get_widget_max_size(self):
        return self.widget_max_size

    def get_combo_box_polygon_type(self):
        return self.combo_box_polygon_type
    
    def get_spin_box_number_poly_per_line(self):
        return self.spin_box_number_poly_per_line
    
#==============================================================================    
#   SETTERS
#==============================================================================
        
    def set_widget(self, widget):
        if(widget):
            self.widget = widget
            
    def set_mainWindow(self, window):
        if(window):
            self.main_window = window
        
    def set_widget_max_size(self, size):
        if(size >= 0):
            self.widget_max_size = size
            
    def set_combo_box_polygon_type(self, combo_box):
        if(combo_box):
            self.combo_box_polygon_type = combo_box

    def set_spin_box_number_poly_per_line(self, spin_box):
        if(spin_box):
            self.spin_box_number_poly_per_line = spin_box
#==============================================================================    
#   METHODS
#==============================================================================
            
    def set_graphic_interface(self):
        
        #To set same size with the window
        self.widget = QtWidgets.QWidget()
        self.widget.resize(260,250)
        
        #Text label TypeOfPoly
        label_polygon_type = QtWidgets.QLabel(self.widget)
        label_polygon_type.setGeometry(QtCore.QRect(40, 20, 200, 20))
        label_polygon_type.setObjectName("label_polygon_type")
        label_polygon_type.setText("Please choose a type of polygon to paint : ")
        
        #Combo Box containing TypeOfPoly
        self.combo_box_polygon_type = QtWidgets.QComboBox(self.widget)
        self.combo_box_polygon_type.setGeometry(QtCore.QRect(50, 40, 161, 22))
        self.combo_box_polygon_type.setObjectName("comboBox")
        self.combo_box_polygon_type.addItem("Triangle")
        self.combo_box_polygon_type.addItem("Square")
        self.combo_box_polygon_type.addItem("Hexagon")
        
        #Spin box to select number of polygon per line [5;+∞[
        self.spin_box_number_poly_per_line = QtWidgets.QSpinBox(self.widget)
        self.spin_box_number_poly_per_line.setGeometry(QtCore.QRect(200, 80, 42, 22))
        self.spin_box_number_poly_per_line.setMinimum(5)
        self.spin_box_number_poly_per_line.setObjectName("spin_box_number_poly_per_line")
        
        #Text label to chose number of polygon per line
        label_polygon_per_line = QtWidgets.QLabel(self.widget)
        label_polygon_per_line.setGeometry(QtCore.QRect(20, 80, 181, 21))
        label_polygon_per_line.setObjectName("label_polygon_per_line")
        label_polygon_per_line.setText("Please choose the number of polygon per line : ")
        
        #Pushbutton to call the click function 
        push_button_draw = QtWidgets.QPushButton(self.widget)
        push_button_draw.setGeometry(QtCore.QRect(90, 150, 90, 50))
        push_button_draw.setObjectName("push_button_draw")
        push_button_draw.setText("Draw !")
        push_button_draw.clicked.connect(self.button_click_action)
        
        #main window of the application
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.setCentralWidget(self.widget)
        self.main_window.resize(260,250)
        self.main_window.show()
        
    def button_click_action(self): 
        
        polygon_type =  self.combo_box_polygon_type.currentText()       
        nb_polygon_per_line = self.spin_box_number_poly_per_line.value()
        
        if (polygon_type == "Square"):
            polygon = sq.Square(self.get_widget_max_size(), nb_polygon_per_line)
            
        elif (polygon_type == "Triangle"):
            polygon = tri.Triangle(self.get_widget_max_size(), nb_polygon_per_line)
        elif (polygon_type == "Hexagon"):
            print("Not finished yet")
            polygon = hexa.Hexagon(self.get_widget_max_size(), nb_polygon_per_line)
            
        tessellation = tess.Tessellation(polygon)
        
        self.main_window.setCentralWidget(tessellation)
        self.main_window.showMaximized()
        
from PyQt5 import QtWidgets, QtCore
from model import saver

class SaveWindow():
    
    def __init__(self, object_to_save):
        
        self.window = QtWidgets.QMainWindow()
        
        self.object_to_save = object_to_save
        
        self.set_graphic_interface()
        
    #Rajouter un truc pour mettre un chemin
    def set_graphic_interface(self):
        
        self.widget = QtWidgets.QWidget()
        
        #Text label filename of the saved tesselation
        label_filename = QtWidgets.QLabel(self.widget)
        label_filename.setGeometry(QtCore.QRect(20, 10, 200, 20))
        label_filename.setObjectName("label_filename")
        label_filename.setText("Please choose a filename to save : ")
        
        #line edit filename of the saved tesselation
        self.line_edit_filename = QtWidgets.QLineEdit(self.widget)
        self.line_edit_filename.setGeometry(QtCore.QRect(20, 40, 100, 20))
        self.line_edit_filename.setObjectName("line_edit_filename ")
            
        #Pushbutton to call the click function 
        push_button_save = QtWidgets.QPushButton(self.widget)
        push_button_save.setGeometry(QtCore.QRect(20, 65, 50, 40))
        push_button_save.setObjectName("push_button_save")
        push_button_save.setText("Save")
        push_button_save.clicked.connect(self.save)
            
    
        self.window.setCentralWidget(self.widget)
        self.window.resize(240,100)
        self.window.show()
        
    def save(self):
        
        if(self.line_edit_filename.text() != ''):
            saver.Saver(self.object_to_save, self.line_edit_filename.text()).save_object()
        else:
            #Text label filename of the saved tesselation
            label_filename = QtWidgets.QLabel(self.widget)
            label_filename.setGeometry(QtCore.QRect(20, 30, 200, 20))
            label_filename.setObjectName("label_filename")
            label_filename.setText("You need to chose a name for your file: ")    
from PyQt5 import QtWidgets
import sys

class SettingsWindow(object):
    
    main_app = QtWidgets.QApplication(sys.argv)
    
    #get the screen size used for the lenght of drawn polygons 
    maxScreenSize = (main_app.primaryScreen().size().width(),
                     main_app.primaryScreen().size().height())
    
    settings_window = QtWidgets.QMainWindow()
    
    def __init__(self):
        
        self.settings_widget = None
        
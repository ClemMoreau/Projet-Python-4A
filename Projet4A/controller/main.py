from controller.settings import Settings
from controller.loadController import LoadController

from view.settingsWindow import SettingsWindow
from view.loadWindow import LoadWindow


from PyQt5 import QtWidgets
import sys

""" Module used to launch the application"""
if __name__ == '__main__':

    SettingsWindow.set_main_app(QtWidgets.QApplication(sys.argv))    

    LoadWindow.set_load_widget(LoadController())
    LoadWindow.show_widget()

    # call the first widget on the windows : settings
    SettingsWindow.set_setting_widget(Settings())
    SettingsWindow.show_widget()
    

    # used to kill everything
    sys.exit(SettingsWindow.get_main_app().exec_())

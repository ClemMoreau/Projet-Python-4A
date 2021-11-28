from view.settingsWindow import SettingsWindow
from view.loadWindow import LoadWindow

from controller.settings import Settings
from controller.loadController import LoadController

from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':

    SettingsWindow.set_main_app(QtWidgets.QApplication(sys.argv))    

    LoadWindow.set_load_widget(LoadController())
    LoadWindow.show_widget()

    # call the first widget on the windows : settings
    SettingsWindow.set_setting_widget(Settings())
    SettingsWindow.show_widget()
    

    # used to kill everything
    sys.exit(SettingsWindow.get_main_app().exec_())

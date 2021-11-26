from view.settingsWindow import SettingsWindow
from controller.settings import Settings
import sys

if __name__ == '__main__':

    # call the first widget on the windows : settings
    setting = Settings()
    SettingsWindow.settings_window.setCentralWidget(setting)

    # used to kill everything
    sys.exit(SettingsWindow.main_app.exec_())

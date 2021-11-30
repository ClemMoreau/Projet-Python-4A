import sys
from PyQt5 import QtWidgets


class SettingsWindow(object):
    
    main_app = None
    
    #get the screen size used for the lenght of drawn polygons 
    max_screen_size = None
    
    settings_widget = None
    
    #==========================================================================
    #   GETTERS
    #==========================================================================
        
    def get_setting_widget():
        return SettingsWindow.settings_widget
    
    def get_max_screen_size():
        return SettingsWindow.max_screen_size
    
    def get_main_app():
        return SettingsWindow.main_app
    
    #==========================================================================
    #   SETTERS
    #==========================================================================
    
    def set_setting_widget(widget):
        if(widget):
            SettingsWindow.settings_widget = widget
            
    def set_max_screen_size(size):
        if(size[0] >=0 and
           size[1] >=0):
            SettingsWindow.max_screen_size = size
            
    def set_main_app(app):
        if(app):
            SettingsWindow.main_app = app
            SettingsWindow.max_screen_size = (app.primaryScreen().size().width(),
                                              app.primaryScreen().size().height())
        
    #==========================================================================
    #   METHODS
    #==========================================================================
    
    def show_widget():
        SettingsWindow.settings_widget.show()
        
    def close_widget():
        SettingsWindow.settings_widget.close()

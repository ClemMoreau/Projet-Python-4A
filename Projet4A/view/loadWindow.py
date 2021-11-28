

class LoadWindow():

    load_widget = None

    def get_load_widget():
        return LoadWindow.load_widget
    
    def set_load_widget(widget):
        if(widget):
            LoadWindow.load_widget = widget
            
    def show_widget():
        LoadWindow.load_widget.show()
        
    def close_widget():
        LoadWindow.load_widget.close()
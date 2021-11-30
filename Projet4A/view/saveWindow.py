

class SaveWindow():

    save_widget = None
    
    #==========================================================================
    #   GETTERS
    #==========================================================================

    def get_save_widget():
        return SaveWindow.save_widget
    
    #==========================================================================
    #   SETTERS
    #==========================================================================
    
    def set_save_widget(widget):
        if(widget):
            SaveWindow.save_widget = widget
            
    #==========================================================================
    #   METHODS
    #==========================================================================        
    
    def show_widget():
        SaveWindow.save_widget.show()
        
    def close_widget():
        SaveWindow.save_widget.close()
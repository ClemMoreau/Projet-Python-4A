

class TessellationWindow():
    
    tessellation = None 
    
    #==========================================================================
    #   GETTERS
    #==========================================================================
    
    def get_tessellation_widget():
        return TessellationWindow.tessellation
    
    #==========================================================================
    #   SETTERS
    #==========================================================================
    
    def set_tessellation_widget(widget):
        if(widget):
            TessellationWindow.tessellation = widget
            
    #==========================================================================
    #   METHODS
    #==========================================================================   
    
    def show_widget():
        TessellationWindow.tessellation.showMaximized()
    
    def close_widget():
        TessellationWindow.tessellation.close()
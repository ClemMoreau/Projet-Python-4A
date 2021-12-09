

class SaveWindow():
    
    # The save widget showed to save tesselation
    save_widget = None
    
    # =========== #
    #   GETTERS   #
    # =========== #
    
    def get_save_widget():
        """
        Getter of the save_widget static attribute
        
        Returns
        -------
        None.

        """
        return SaveWindow.save_widget
    
    # =========== #
    #   SETTERS   #
    # =========== #
    
    def set_save_widget(widget):
        """
        Setter of the save_wiget static attribute

        Parameters
        ----------
        widget : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        if(widget):

            SaveWindow.save_widget = widget
            
    # =========== #
    #   METHODS   #
    # =========== #       
    
    def show_widget():
        """
        Show the save_widget

        Returns
        -------
        None.

        """
        
        SaveWindow.save_widget.show()
        
    def close_widget():
        """
        Close the save_widget

        Returns
        -------
        None.

        """
        
        SaveWindow.save_widget.close()
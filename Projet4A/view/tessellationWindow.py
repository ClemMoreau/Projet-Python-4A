

class TessellationWindow():
    """
    Static class which represent the settings window,
    used by users to set param for the tessellation

    Methods
    ---------------

    show_widget()
        method which show the widget
    close_widget()
        method which close the widget
    """

    # the tessellation widget
    tessellation_widget = None

    # =========== #
    #   GETTERS   #
    # =========== #

    def get_tessellation_widget():
        """
        Getter of the tessellation_widget attribute.

        Returns
        -------
        TESSELLATION.

        """
        return TessellationWindow.tessellation_widget

    # =========== #
    #   SETTERS   #
    # =========== #

    def set_tessellation_widget(widget):
        """
        Setter of the tessellation_widget attribute.

        Parameters
        ----------
        widget : TESSELLATION.

        Returns
        -------
        None.

        """
        if(widget):
            TessellationWindow.tessellation_widget = widget

    # =========== #
    #   METHODS   #
    # =========== #

    def show_widget():
        """
        Method wich show the tessellation_widget

        Returns
        -------
        None.

        """
        TessellationWindow.tessellation_widget.showMaximized()

    def close_widget():
        """
        Method wich close the tessellation_widget

        Returns
        -------
        None.

        """
        TessellationWindow.tessellation_widget.close()

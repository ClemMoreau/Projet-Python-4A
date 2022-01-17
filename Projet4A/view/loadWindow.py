

class LoadWindow():
    """
    Class which represent the loading window,
    used by users to load a tessellation

    Methods
    ---------------

    show_widget()
        method which show the widget
    close_widget()
        method which close the widget
    """

    # The load_widget showed to load tesselation
    load_widget = None

    # =========== #
    #   GETTERS   #
    # =========== #

    def get_load_widget():
        """
        Getter of the load_widget attribute.

        Returns
        -------
        LOADCONTROLLER.

        """
        return LoadWindow.load_widget

    # =========== #
    #   SETTERS   #
    # =========== #

    def set_load_widget(widget):
        """
        Setter of the load_widget attribute.

        Parameters
        ----------
        widget : LOADCONTROLLER.

        Returns
        -------
        None.

        """
        if(widget):
            LoadWindow.load_widget = widget

    # =========== #
    #   METHODS   #
    # =========== #

    def show_widget():
        """
        Method which show the load_widget

        Returns
        -------
        None.

        """
        LoadWindow.load_widget.show()

    def close_widget():
        """
        Method which close the load_widget

        Returns
        -------
        None.

        """
        LoadWindow.load_widget.close()

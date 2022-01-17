

class SettingsWindow(object):
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

    # Main application mandatory to show window
    main_app = None

    # Screen size used for the lenght of drawn polygons
    max_screen_size = None

    # Settings widget to allow user to select parameters for the tessellation
    settings_widget = None

    # =========== #
    #   GETTERS   #
    # =========== #

    def get_setting_widget():
        """
        Getter for the setting_widget static atttribute

        Returns
        -------
        settings_widgets : Settings
            Settings widget to allow user
            to select parameters for the tessellation.

        """

        return SettingsWindow.settings_widget

    def get_max_screen_size():
        """
        Getter for the max_screen_size static attribute

        Returns
        -------
        max_screen_size : tuple<int>
            Screen size used for the lenght of drawn polygons.

        """

        return SettingsWindow.max_screen_size

    def get_main_app():
        """
        Getter for the main_app static attribute

        Returns
        -------
        main_app : QApplication
            Main application mandatory to show window.

        """

        return SettingsWindow.main_app

    # =========== #
    #   SETTERS   #
    # =========== #

    def set_setting_widget(widget):
        """
        Setter for the setting_widget

        Parameters
        ----------
        widget : QWidget
            Screen size used for the lenght of drawn polygons.

        Returns
        -------
        None.

        """

        if(widget):
            SettingsWindow.settings_widget = widget

    def set_max_screen_size(size):
        """
        Setter for the max_screen_size static attribute

        Parameters
        ----------
        size : tuple<int>
            DESCRIPTION.

        Returns
        -------
        None.

        """

        if(size[0] >= 0 and
           size[1] >= 0):

            SettingsWindow.max_screen_size = size

    def set_main_app(app):
        """
        Setter for the main_app static attribute

        Parameters
        ----------
        app : QApplication
            Main application mandatory to show windows.

        Returns
        -------
        None.

        """
        if(app):
            SettingsWindow.main_app = app
            screen_size = (app.primaryScreen().size().width(),
                           app.primaryScreen().size().height())
            SettingsWindow.max_screen_size = screen_size

    # =========== #
    #   METHODS   #
    # =========== #

    def show_widget():
        """
        Method which show the settings_widget

        Returns
        -------
        None.

        """

        SettingsWindow.settings_widget.show()

    def close_widget():
        """
        Method which close the settings_widget

        Returns
        -------
        None.

        """

        SettingsWindow.settings_widget.close()

import pickle


class Loader():
    """
    Class which take a saved file 
    and reuse the data inside of it
    
    Attributes
    ----------
    path : STRING
        Path where the file to load is
    
    filename : STRING
        Filename of the file to load
    
    object_loaded : OBJECT
        Object loaded in the file
    
    Methods 
    ---------------
    
    load_object()
         method which open a saved file
         and read the binary data inside
    
    """
        
        #================ #
        #   CONSTRUCTOR   #
        #================ #
 
    def __init__(self, filename, path = None):
        """
        Parameters
        ---------------
        
        filename : str
            name of the file (.txt)
        path : str
            path to the place where the file is saved
            
        """
        
        self.path = path
        
        self.filename = filename
        
        self.object_loaded = None
            
        # =========== #
        #   GETTERS   #
        # =========== #

    def get_path(self):
        """
        Getter of the path attribute

        Returns
        -------
        self.path : STRING
            Path where the file to load is.

        """
        
        return self.path
    
    def get_filename(self):
        """
        Getter of the filename attribute

        Returns
        -------
        self.filename : STRING
            Name of the file to load.

        """
        
        return self.filename

    def get_object_loaded(self):
        """
        Getter of the object_to_save attribute

        Returns
        -------
        self.object_to_save : OBJECT
            The object contained in the file loaded.

        """
        
        return self.object_loaded
    
        # =========== #
        #   SETTERS   #
        # =========== #
        
    def set_path(self, path):
        """
        Setter of the path attribute

        Parameters
        ----------
        path : STRING
            new path where the file to load is.

        Returns
        -------
        None.

        """
        
        self.path = path
        
    def set_filename(self, filename):
        """
        Setter of the filename attribute

        Parameters
        ----------
        filename : STRING
            name of the new file to load.

        Returns
        -------
        None.

        """
        
        self.filename = filename
 
    def set_object_loaded(self, obj):
        """
        Setter of the object_loaded attribute

        Parameters
        ----------
        obj : OBJECT
            new object loaded.

        Returns
        -------
        None.

        """
        
        if(obj != None):
            self.object_loaded = obj

        # =========== #
        #   METHODS   #
        # =========== #
          
    def load_object(self):
        """
        Method which open a saved file
        and read the binary data inside

        Returns
        -------
        None.

        """
        
        file = open(self.path + self.filename,"rb")
        
        # Load the object in the file
        self.object_loaded = pickle.load(file)
        
        file.close()

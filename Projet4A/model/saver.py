import pickle

class Saver():
    """
    Class which aim to save the deformation
    apllied to the figure
    
    Methods
    ---------------
    
    clear_file()
        method which clear the file associate with self
    save_object()
        save the object into a file
        the object is converted into binary data
    """
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
 
    def __init__(self, object_to_save, filename, path = None):
        """
        Parameters
        ---------------
        
        object_to_save : object
            the object that the user want to save
        filename : str
            name of the file
        path : str
            path to the place where the file is saved
            
        """
        
        # Path where file is saved
        self.path = path
        
        # Filename of the file to save
        self.filename = filename
        
        # Tesselation to save
        self.object_to_save = object_to_save
        
    # =========== #
    #   GETTERS   #
    # =========== #

    def get_path(self):
        """
        Getter of the path attribute

        Returns
        -------
        self.path : string
            Path where file is saved.

        """

        return self.path
    
    def get_filename(self):
        """
        Getter of the filename attribute

        Returns
        -------
        self.filename : STRING
            Filename of the file to save.

        """
        
        return self.filename
    
    def get_object_to_save(self):
        """
        Getter of the object_to_save attribute

        Returns
        -------
        self.object_to_save : OBJECT 
            Tesselation to save.

        """
        return self.object_to_save

    # =========== #
    #   SETTERS   #
    # =========== #
    
    def set_path(self, path):
        """
        Setter of the path attribute

        Parameters
        ----------
        path : STRING
            new location where save.

        Returns
        -------
        None.

        """
        
        self.path = path
        
    def set_filename(self, filename):
        """
        Setter of the filename

        Parameters
        ----------
        filename : STRING
            name of the file saved.

        Returns
        -------
        None.

        """

        self.filename = filename
        
    def set_object_to_save(self, obj):
        """
        Setter of the object_to_save

        Parameters
        ----------
        obj : OBJECT
            the new object to save in the file.

        Returns
        -------
        None.

        """        
        
        if(obj != None):
            self.object_to_save = obj
 
    # =========== #
    #   METHODS   #
    # =========== #

    def clear_file(self):
        """
        Method which clear the file where object is saved

        Returns
        -------
        None.

        """
        
        file = open(self.path + self.filename + '.txt','w')
        file.close()
        
    def save_object(self):
        """
        Save the object into a file
        The object is converted into binary data

        Returns
        -------
        None.

        """
        if(self.object_to_save != None):
            
            # Before saving, file need to be empty
            self.clear_file()
            
            file = open(self.path + self.filename + '.txt',"wb")
            
            # Object saved in the file
            pickle.dump(self.object_to_save, file)
            
            file.close()

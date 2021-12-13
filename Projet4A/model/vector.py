import math
import numpy as np


class Vector(object):
    """
    Class which represent vector
    
    Attributes
    ----------
    start_point : QPOINT
    Starting point of the vector
    
    end_point : QPOINT
    Ending point of the vector
    
    vector : TUPLE<FLOAT>
    Components of the vector
    
    Methods
    ---------------
    line_to_vector(line_start_point, line_end_point)
        Method which calculate the components of the vector 
        (line_start_point, line_end_point)
        
    vector_length()
        Method which return the length of a given vector in param
        
    distance_point_line(point)
        Method which calculate the distance between 
        the point in param and self object
    """
    
        # =============== #
        #   CONSTRUCTOR   #
        # =============== #
    
    def __init__(self, start_point, end_point):
        """
        Constructor of the Vector class
        Initalize the vector with the params

        Parameters
        ----------
        start_point : QPOINT
            Starting point of the vector.
        end_point : QPOINT
            Ending point of the vector.

        Returns
        -------
        None.

        """    
        
        # Starting point of the vector
        self.start_point = start_point
        
        # Ending point of the vector
        self.end_point = end_point
        
        # Components of the vector
        self.vector = self.line_to_vector(start_point, end_point)
        
        # =========== #
        #   GETTERS   #
        # =========== #
        
    def get_start_point(self):
        """
        Getter of the start_point attribute

        Returns
        -------
        QPOINT
            Starting point of the vector.

        """
        return self.start_point
    
    def get_end_point(self):
        """
        Getter of the end_point attribute

        Returns
        -------
        QPOINT
            Ending point of the vector.

        """
        return self.end_point
    
    def get_vector(self):
        """
        Getter of the vector attribute

        Returns
        -------
        TUPLE<FLOAT>
            Components of the vector.

        """
        return self.vector
    
        # =========== #
        #   SETTERS   #
        # =========== #
        
    def set_start_point(self, point):
        """
        Setter of the start_point attribute

        Parameters
        ----------
        point : QPOINT
            New starting point of the vector.

        Returns
        -------
        None.

        """
        
        if(point):
            
            self.start_point = point
            self.vector = self.line_to_vector(self.start_point, self.end_point)
            
    def set_end_point(self, point):
        """
        Setter of the end_point attribute

        Parameters
        ----------
        point : QPOINT
            New ending point of the vector.

        Returns
        -------
        None.

        """
        
        if(point):
            self.end_point= point
            self.vector = self.line_to_vector(self.start_point, self.end_point)
        
    def set_vector(self, vector):
        """
        Setter of the vector attribute

        Parameters
        ----------
        vector : TUPLE<FLOAT>
            new components of the vector.

        Returns
        -------
        None.

        """
        
        if(vector):
            self.vector = vector
            
        # =========== #
        #   METHODS   #
        # =========== #
        
    def line_to_vector(self, line_start_point, line_end_point):
        """
        Method which calculate the components of the vector 
        (line_start_point, line_end_point)

        Parameters
        ----------
        line_start_point : QPOINT
            Starting point of the vector.
        line_end_point : QPOINT
            Ending point of the vector.

        Returns
        -------
        TUPLE<FLOAT>
            Components of the vector.

        """
        return (line_end_point.x() - line_start_point.x(),
                line_end_point.y() - line_start_point.y())
    
    def vector_length(self):
        """
        Method which return the length of a given vector in param

        Returns
        -------
        FLOAT
            the length of the given vector in param.

        """
        return math.sqrt(self.vector[0]**2 + self.vector[1]**2)

    def distance_point_line(self, point):
        """
        Method which calculate the distance between 
        the point in param and self object

        Parameters
        ----------
        point : QPOINT
            DESCRIPTION.

        Returns
        -------
        TUPLE<FLOAT>
            Distance between point in param and self.

        """
        
        # Check if the point is between segment terminals 
        X = (min(self.end_point.x(), self.start_point.x()),
             max(self.end_point.x(), self.start_point.x()))
        Y = (min(self.end_point.y(), self.start_point.y()),
             max(self.end_point.y(), self.start_point.y()))
        
        # If the line is vertical or horizontal
        if (X[0] == X[1] or Y[0] == Y[1]):
            # add margin to detect were a point is near the vector
            margin = 5
            
        else:
            margin = 0
            
        # Check if the point is "inside" the vector
        if(X[0] - margin < point.x() < X[1] + margin and 
           Y[0] - margin < point.y() < Y[1] + margin):
        
            line_vector = np.array(self.line_to_vector(self.start_point, self.end_point))
            
            vector_to_projeted = np.array(self.line_to_vector(self.start_point, point))
        
            # Calculate the projected vector of self
            projected_vector = (np.dot(vector_to_projeted, line_vector) / np.dot(line_vector, line_vector))*line_vector
            
            # Calculate the distance between the point and the vector
            return (vector_to_projeted - projected_vector)

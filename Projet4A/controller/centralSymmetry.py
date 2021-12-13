from PyQt5 import QtCore

from model.vector import Vector


class CentralSymmetry(object):
    """
    Class that represent the central symmetry of a polygon
    
    Methods 
    ---------------
    calculate_middle_point(polygon):
        Method which calculate the center of the polygon in parameter
        
    calculate_central_symmetry(point, indice_of_poly):
        Method which calculate the symmetry of the given point in param
    
    """
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    
    def __init__(self, fixed_points, polygon_list):
        """
        Construtor of the CentralSymmetry class

        Parameters
        ----------
        fixed_points : list<QPoint>
            list of the fixed point in the tesselation
            used to calculate the center of each polygon.
        polygon_list : list<QPolygon>
            list of polygon 
            used to calculate their center of gravity.

        Returns
        -------
        None.

        """  
        
        # Fixed point of the polygon, used to calculate center
        self.fixed_points = fixed_points
        
        # Calcul of the center of each polygon
        self.middle_points = []
        for polygon in polygon_list:
            self.middle_points.append(self.calculate_middle_point(polygon))
            
    # =========== #
    #   GETTERS   #
    # =========== #            
      
    def get_fixed_points(self):
        """
        Getter of the fixed_points attribute

        Returns
        -------
        self.fixed_points : list<QPoint>
            list of the fixed point of the polygon in the tesselation.

        """
        return self.fixed_points
    
    def get_middle_points(self):
        """
        Getter of the middle_points attribute

        Returns
        -------
        self.middle_points : list<QPointF>
            center of each polygon in the tesselation.

        """
        
        return self.middle_points

    # =========== #
    #   SETTERS   #
    # =========== #  
    
    def set_fixed_points(self, fixed_points):
        """
        Setter of the fixed_points attribute

        Parameters
        ----------
        fixed_points : list<QPoint>
            new fixed point of the polygon in the tesselation.

        Returns
        -------
        None.

        """
        
        self.fixed_points = fixed_points
        
    def set_middle_points(self, middle_points):
        """
        Setter of the middle_point attribute

        Parameters
        ----------
        middle_points : list<QPoint>
            new center of each polygon in the tesselation.

        Returns
        -------
        None.

        """
        
        self.middle_points = middle_points

    # =========== #
    #   METHODS   #
    # =========== #
    
    def calculate_middle_point(self, polygon):
        """
        Method which calculate the center of the polygon in parameter

        Parameters
        ----------
        polygon : QPolygon
            Polygon to calculate his center.

        Returns
        -------
        QPOINT
            the center of the polygon given in param.

        """
        
        middle_point = QtCore.QPointF()
        fixed_point_number = 0
        
        # For each point in the polygon
        for point in polygon:
            
            # We used only fixed points to consider only regular polygon,
            if (point in self.fixed_points):
                
                middle_point += point
                fixed_point_number += 1
                
        # middle point is the average of the coordinate of a regular polygon
        return middle_point/fixed_point_number
    
    def calculate_central_symmetry(self, point, indice_of_poly):
        """
        Method which calculate the symmetry of the given point in param

        Parameters
        ----------
        point : QPOINT
            Point to calculate symmetry.
        indice_of_poly : INT
            indice of polygon in the list
            used to get the correct center in the list.

        Returns
        -------
        QPOINT
            the symmetry of the point given in param.

        """
        
        # Get the middle corresponding to the polygon
        mid_point = self.middle_points[indice_of_poly]
        
        # Initialize a vector from point to mid_point
        vector = Vector(point, mid_point)
        
        # Calcul of the symmetry : the vector is added once again
        sym_point = QtCore.QPointF(mid_point.x() + vector.get_vector()[0],
                                   mid_point.y() + vector.get_vector()[1])
            
        return QtCore.QPoint(sym_point.x(),
                             sym_point.y())
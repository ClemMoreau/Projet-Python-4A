
from PyQt5 import QtCore

class AxialSymmetry(object):
    """
    Attributes
    ----------
    fixed_points : list<QPoint>
        Non-modifiable point of the tessellation.
    polygon_list : list<QPolygon>
        Polygons of the tessellation.
    
    Methods
    ---------------
    calculate_axial_point()
        This methods calculate symmetry axe
    calculate_axial_symmetry()
       This methods calculate the symmetry of a point
    """
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    
    def __init__(self, fixed_points, polygon_list):
        """
        Constructor of the AxialSymmetry class,
        used to calculate symmetry axe for all the polygons in polygon_list

        Parameters
        ----------
        fixed_points : list<QPoint>
            Non-modifiable point of the tessellation.
        polygon_list : list<QPolygon>
            Polygons of the tessellation.

        Returns
        -------
        None.

        """
      
        self.fixed_points = fixed_points
      
        self.axial_points = []
        for polygon in polygon_list:
            self.axial_points.append(self.calculate_axial_point(polygon))
          
    # =========== #
    #   GETTERS   #
    # =========== #
    
    def get_fixed_points(self):
        """
        Getter of the fixed_points attribute.

        Returns
        -------
        list<QPoint>
            Non modifiable points in the tessellation.

        """
        return self.fixed_points
        
    def get_axial_points(self):
        """
        Getter of the axial_points attribute.

        Returns
        -------
        list<QPoint>
            points used as symmetry axe.

        """
        return self.axial_points
    
    # =========== #
    #   SETTERS   #
    # =========== #
    
    def set_fixed_points(self, points):
        """
        Setter of the fixed_points attribute.

        Parameters
        ----------
        points : list<QPoint>
            the new non modifiable points in the tessellation.

        Returns
        -------
        None.

        """
        self.fixed_points = points
    
    def set_axial_points(self, points):
        """
        Setter of the axial_points attribute.

        Parameters
        ----------
        points : list<QPoint>
            the new points used as symmetry axe.

        Returns
        -------
        None.

        """
        self.axial_points = points
    
    # =========== #
    #   METHODS   #
    # =========== #
    
    def calculate_axial_point(self, polygon):
        """
        Method which calculate the point used as symmetry axe of the polygon
        in param

        Parameters
        ----------
        polygon : QPolygon
            polygon to calculate symmetry axe.

        Returns
        -------
        QPoint
            point used as symmetry axe.

        """
        axial_point = QtCore.QPointF()
        fixed_point_number = 0

        for point in polygon:
            if (point in self.fixed_points):
                axial_point += point
                fixed_point_number += 1
        
        return axial_point/fixed_point_number


    def calculate_axial_symmetry(self, point, indice_of_poly):
        """
        Method which calculate the symmetry of the point given in param.

        Parameters
        ----------
        point : QPoint
            point which we want the symmetry.
        indice_of_poly : int
            indice of the polygone in the polygon list of the tessellation.

        Returns
        -------
        QPoint
            the symmetry of the point in param.

        """
        axial_point = self.axial_points[indice_of_poly]
        sym_point = QtCore.QPointF(axial_point.x() + abs(axial_point.x() - point.x()) ,
                                   point.y())
        
        return QtCore.QPoint(sym_point.x(),
                             sym_point.y())
    
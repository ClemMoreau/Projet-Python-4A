from PyQt5 import QtCore

from model.vector import Vector


class CentralSymmetry(object):
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    
    def __init__(self, fixed_points, polygon_list):
        
        self.fixed_points = fixed_points
        
        self.middle_points = []
        for polygon in polygon_list:
            self.middle_points.append(self.calculate_middle_point(polygon))
        
        self.symmetry_indice = -1
        
    def get_symmetry_indice(self):
        return self.symmetry_indice
    
    def set_symmetry_indice(self, indice):
        self.symmetry_indice = indice
        
    def calculate_middle_point(self, polygon):
        middle_point = QtCore.QPointF()
        fixed_point_number = 0
        
        for point in polygon:
            if (point in self.fixed_points):
                middle_point += point
                fixed_point_number += 1
        return middle_point/fixed_point_number
    
    def calculatre_central_symmetry(self, point, indice_of_poly):
        mid_point = self.middle_points[indice_of_poly]
        vector = Vector(point, mid_point)
        sym_point = QtCore.QPointF(mid_point.x() + vector.get_vector()[0],
                                   mid_point.y() + vector.get_vector()[1])
            
        return QtCore.QPoint(sym_point.x(),
                             sym_point.y())
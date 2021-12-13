
from PyQt5 import QtCore

class AxialSymmetry(object):
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    
    def __init__(self, fixed_points, polygon_list):
      
      self.fixed_points = fixed_points
      
      self.axial_points = []
      for polygon in polygon_list:
          self.axial_points.append(self.calculate_axial_point(polygon))
      
      self.symmetry_indice = -1
        
    def get_symmetry_indice(self):
        return self.symmetry_indice
    
    def set_symmetry_indice(self, indice):
        self.symmetry_indice = indice
        
    def calculate_axial_point(self, polygon):
        axial_point = QtCore.QPointF()
        fixed_point_number = 0
        
        for point in polygon:
            if (point in self.fixed_points):
                axial_point += point
                fixed_point_number += 1
        return axial_point/fixed_point_number
    
    
    def calculate_axial_symmetry(self, point, indice_of_poly):
        axial_point = self.axial_points[indice_of_poly]
        sym_point = QtCore.QPointF(axial_point.x() + abs(axial_point.x() - point.x()) ,
                                   point.y())
            
        return QtCore.QPoint(sym_point.x(),
                             sym_point.y())
    
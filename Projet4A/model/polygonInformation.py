from model.square import Square
from model.triangle import Triangle
from model.hexagon import Hexagon

from view.settingsWindow import SettingsWindow


class PolygonInformation(object):
    
    #==========================================================================
    #   CONSTRUCTOR
    #==========================================================================

    def __init__(self, polygon_type, nb_polygon_per_line):
        
        
        if (polygon_type == "Square"):
            polygon = Square(SettingsWindow.max_screen_size, 
                             nb_polygon_per_line)
        elif (polygon_type == "Triangle"):
            polygon = Triangle(SettingsWindow.max_screen_size, 
                               nb_polygon_per_line)
        elif (polygon_type == "Hexagon"):
            polygon = Hexagon(SettingsWindow.max_screen_size,
                              nb_polygon_per_line)
        
        self.polygon = polygon
        
        self.polygon_type = (str(type(polygon)))
        
        self.polygon_list = self.polygon.generate_poly()
        
        self.polygon_coordinate = [[] for i in range(self.get_polygon().get_size()[1] + 1)]
        self.generate_coordinates()
        
        self.fixed_points = []
        self.generate_non_modifiable_point()
        
    #==========================================================================
    #   GETTERS
    #==========================================================================
    def get_polygon(self):
        return self.polygon
    
    def get_polygon_type(self):
        return self.polygon_type
    
    def get_polygon_list(self):
        return self.polygon_list
    
    def get_polygon_in_list(self, indice):
        if(0 <= indice < len(self.polygon_list)):
            return self.polygon_list[indice]
    
    def get_polygon_coordinate(self):
        return self.polygon_coordinate
    
    def get_fixed_points(self):
        return self.fixed_points

    #==========================================================================
    #   SETTERS
    #==========================================================================

    def set_polygon(self, polygon):
        self.polygon = polygon

    def set_polygon_type(self, polygon_type):
        if(polygon_type):
            self.polygon_type = polygon_type

    def set_polygon_list(self, polygon_list):
        self.polygon_list = polygon_list
        
    def set_polygon_in_list(self, indice, polygon):
        if(0 <= indice < len(self.polygon_list)):
            self.polygon_list[indice] = polygon

    def set_polygon_coordinate(self, polygon_coordinate):
        self.polygon_coordinate = polygon_coordinate
        
    def set_fixed_points(self, fixed_points):
        self.fixed_points = fixed_points

    #==========================================================================
    #   METHODS
    #==========================================================================  
      
    def generate_coordinates(self):
        
        for poly in self.polygon_list:
            for j in range(poly.count()):
                if (0 <= poly.at(j).y() <= self.polygon.size[1] + 1): 
                    self.polygon_coordinate[int(poly.at(j).y())].append(poly)
                    
                    
    def generate_non_modifiable_point(self):
        
        for poly in self.polygon_list:
            for i in range(0,poly.count()):
                self.fixed_points.append(poly.at(i))
                
    def can_move(self,point):
    
        if(self.fixed_points.count(point) != 0):
                return False
        return True
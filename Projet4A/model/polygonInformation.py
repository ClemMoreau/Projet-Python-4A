from model.polygon import Polygon

class PolygonInformation(object):
    
    def __init__(self, polygon):
        
        self.polygon = polygon
        
        self.typeofPolygon = str(type(polygon))
        
        self.polygon_list = self.polygon.generate_poly()    
        
        
        self.polygon_coordinate = [[] for i in range(polygon.size[1] + 1)]
        self.generate_coordinates()
        
        self.fixed_points = []
        self.generate_non_modifiable_point()
        
    def get_polygon_list(self):
        return self.polygon_list
    
    def get_polygon_coordinate(self):
        return self.polygon_coordinate
    
    def set_polygon_list(self, polygon_list):
        self.polygon_list = polygon_list
        
    def generate_coordinates(self):
        
        for poly in self.polygon_list:
            for j in range(poly.count()):
                if (0 <= poly.at(j).y() <= self.polygon.size[1] + 1): 
                    self.polygon_coordinate[int(poly.at(j).y())].append(poly)
                    
    def generate_non_modifiable_point(self):
        
        for poly in self.polygon_list:
            for i in range(0,poly.count()):
                self.fixed_points.append(poly.at(i))
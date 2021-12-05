from model.square import Square
from model.triangle import Triangle
from model.hexagon import Hexagon
from model.vector import Vector
from controller.centralSymmetry import CentralSymmetry

from view.settingsWindow import SettingsWindow

from PyQt5 import QtCore

class PolygonInformation(object):
    
    #==========================================================================
    #   CONSTRUCTOR
    #==========================================================================

    def __init__(self, polygon_type, nb_polygon_per_line , central_symmetry):
        
        
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
        
        self.central_symmetry = None
        
        if (central_symmetry):
            self.central_symmetry = CentralSymmetry(self.fixed_points, self.polygon_list)
        
        self.added_point = False
        
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
    
    def add_point_to_all(self, point, indice_in_poly, indice_of_poly):
        
        vector = Vector(self.polygon_list[indice_of_poly].at(indice_in_poly - 1), point)  
        
        for j in range(0,len(self.polygon_list)):
            
           point = QtCore.QPoint(vector.get_vector()[0] + self.polygon_list[j].at(indice_in_poly - 1).x(),
                                  vector.get_vector()[1] + self.polygon_list[j].at(indice_in_poly - 1).y())
           
           self.polygon_list[j].insert(indice_in_poly,point)
           
           
           if (self.central_symmetry):
               
               symmetry_indice = ((self.polygon_list[j].count() - 1)//2 + indice_in_poly) % (self.polygon_list[j].count() - 1)
               
               if indice_in_poly < (self.polygon_list[j].count() - 1)//2:
                   symmetry_indice +=1
               
               if indice_in_poly == (self.polygon_list[j].count() - 1)//2:
                   symmetry_indice = self.polygon_list[j].count()
                   
               sypoint = self.central_symmetry.calculatre_central_symmetry(point, j)
              
               self.polygon_list[j].insert(symmetry_indice,sypoint)
               self.central_symmetry.set_symmetry_indice(symmetry_indice)
               

    def modify_point_in_all(self, new_point, indice_in_poly, indice_of_poly):
        
        vector = Vector(self.polygon_list[indice_of_poly].at(indice_in_poly - 1), new_point)  
        
        for j in range(0,len(self.polygon_list)):
            
            point = QtCore.QPoint(vector.get_vector()[0] + self.polygon_list[j].at(indice_in_poly - 1).x(),
                                   vector.get_vector()[1] + self.polygon_list[j].at(indice_in_poly - 1).y())
            
            if (self.central_symmetry):
                sypoint = self.central_symmetry.calculatre_central_symmetry(point, j)
                
                symmetry_indice = self.central_symmetry.get_symmetry_indice()
                symmetry_indice = ((self.polygon_list[j].count() - 2)//2 + indice_in_poly) % (self.polygon_list[j].count() - 2)
                
                if indice_in_poly < (self.polygon_list[j].count() - 2)//2:
                    symmetry_indice +=1
                
                if indice_in_poly == (self.polygon_list[j].count() - 2)//2:
                    symmetry_indice = self.polygon_list[j].count() - 1
                
                indice = indice_in_poly 
                
                if(symmetry_indice < indice_in_poly and self.added_point):
                    indice += 1
                    
                if(symmetry_indice < indice_in_poly and not self.added_point):
                    symmetry_indice -= 1    
                    
                    
                self.polygon_list[j].replace(indice,point)
                self.polygon_list[j].replace(symmetry_indice,sypoint)
                
            else:
                self.polygon_list[j].replace(indice_in_poly,point)

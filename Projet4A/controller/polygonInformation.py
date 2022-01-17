from model.square import Square
from model.triangle import Triangle
from model.hexagon import Hexagon
from model.vector import Vector

from controller.centralSymmetry import CentralSymmetry
from controller.axialSymetry import AxialSymmetry

from view.settingsWindow import SettingsWindow

from PyQt5 import QtCore

class PolygonInformation(object):
    """
    
    Class which represent all the operation and data of the polygons
    to give them to the tessellation for drawing
    
    
    Attributes
    ----------
    polygon_type : STRING
        type of the current polygon 
        
    polygon_list : LIST<QPOLYGON>
    
    polygon_coordinate : LIST<LIST<QPOLYGON>>
        list of the polygon, sorted by their y coordinate 
    
    fixed_points : LIST<QPOINT>
        list of points that user can not move during deformation
    
    central_symmetry : CENTRALSYMMETRY
        used to get methods to calculate central symmetry in the polygons
        
    added_point : BOOL
        true if point is added by user by a mousse press
    
    Methods
    ---------------
    generate_coordinates():
        Method which sort polygon in polygon_coordinate list using their y coordinate
    generate_non_modifiable_point():
        Method which put initial point in the fixed_point list
    can_move():
        Method which return if a point is allow to move
    add_point_to_all(point, indice_in_poly, indice_of_poly):
        Method which add point to polygons
    modify_point_in_all(new_point, indice_in_poly, indice_of_poly):
        Method which move point in polygons
    
    """
    
        # =============== #
        #   CONSTRUCTOR   #
        # =============== #

    def __init__(self, polygon_type, nb_polygon_per_line , central_symmetry, axial_symmetry):
        """
        Constructor of the PolygonInformation class

        Parameters
        ----------
        polygon_type : STRING
            Type of the polygon draw in the tesselation.
        nb_polygon_per_line : INT
            number of polygon per line on the screen.
        central_symmetry : BOOL
            Boolean used to check if the tesselation 
            have to add central symmetry to the deformation.

        Returns
        -------
        None.

        """
        
        #mettre un switch
        if (polygon_type == "Square"):
            polygon = Square(SettingsWindow.max_screen_size, 
                             nb_polygon_per_line)
        elif (polygon_type == "Triangle"):
            polygon = Triangle(SettingsWindow.max_screen_size, 
                               nb_polygon_per_line)
        elif (polygon_type == "Hexagon"):
            polygon = Hexagon(SettingsWindow.max_screen_size,
                              nb_polygon_per_line)
        
        self.polygon_type = (str(type(polygon)))
        
        self.polygon_list = polygon.generate_poly()
        
        self.polygon_coordinate = [[] for i in range(polygon.get_size()[1] + 1)]
        self.generate_coordinates()
        
        self.fixed_points = []
        self.generate_non_modifiable_point()
        
        self.central_symmetry = None
        
        if (central_symmetry):
            self.central_symmetry = CentralSymmetry(self.fixed_points, self.polygon_list)
        
        self.axial_symmetry = None 
        if (axial_symmetry):
            self.axial_symmetry = AxialSymmetry(self.fixed_points, self.polygon_list)
            
        self.added_point = False
            
        # =========== #
        #   GETTERS   #
        # =========== #
        
    def get_polygon_type(self):
        """
        Getter of the polygon_type attribute

        Returns
        -------
        STRING
            Type of the polygon draw, selected by user in the setting widget.

        """
        
        return self.polygon_type
    
    def get_polygon_list(self):
        """
        Getter of the polygon_list attribute

        Returns
        -------
        LIST<QPOLYGON>
            List of the polygon to draw.

        """
        return self.polygon_list
    
    def get_polygon_in_list(self, indice):
        """
        Getter of the polygon_in_list attribute

        Parameters
        ----------
        indice : INT
            Indice of the polygon in the polygon_list attribute.

        Returns
        -------
        QPOLYGON
            Polygon at indice indice in the polygon_list.

        """
        
        if(0 <= indice < len(self.polygon_list)):
            
            return self.polygon_list[indice]
    
    def get_polygon_coordinate(self):
        """
        Getter of the polygon_coordinate attribute

        Returns
        -------
        LIST<LIST<QPolygon>>
            DESCRIPTION.

        """
        return self.polygon_coordinate
    
    def get_fixed_points(self):
        """
        Getter of the fixed_points attribute

        Returns
        -------
        LIST<QPOINT>
            Non-modifiable point in the tesselation.

        """
        
        return self.fixed_points

        # =========== #
        #   SETTERS   #
        # =========== #

    def set_polygon_type(self, polygon_type):
        """
        Setter of the polygon_type attribute

        Parameters
        ----------
        polygon_type : STRING
            new polygon type.

        Returns
        -------
        None.

        """
        if(polygon_type):
            
            self.polygon_type = polygon_type

    def set_polygon_list(self, polygon_list):
        """
        Setter of the polygon_list attribute,
        used to change the list

        Parameters
        ----------
        polygon_list : LIST<QPOLYGON>
            new list of polygon to draw in the tesselation.

        Returns
        -------
        None.

        """
        self.polygon_list = polygon_list
        
    def set_polygon_in_list(self, indice, polygon):
        """
        Setter of the polygon_list attribute,
        used to change only one polygon in the list

        Parameters
        ----------
        indice : INT
            Indice of the polygon in the polygon_list.
        polygon : QPOLYGON
            new polygon to replace in the polygon_list at indice indice.

        Returns
        -------
        None.

        """
        if(0 <= indice < len(self.polygon_list)):
            
            self.polygon_list[indice] = polygon

    def set_polygon_coordinate(self, polygon_coordinate):
        """
        Setter of the polygon_coordinate attribute

        Parameters
        ----------
        polygon_coordinate : LIST<LIST<QPOLYGON>>
            new list containing polygon sort by their coordinate in ordinate.

        Returns
        -------
        None.

        """
        
        self.polygon_coordinate = polygon_coordinate
        
    def set_fixed_points(self, fixed_points):
        """
        Setter of the fixed_points attribute

        Parameters
        ----------
        fixed_points : LIST<QPOINT>
            list of the initial points of the tesselation,
            those point can not be moved during execution.

        Returns
        -------
        None.

        """
        
        self.fixed_points = fixed_points

        # =========== #
        #   METHODS   #
        # =========== #
      
    def generate_coordinates(self):
        """
        Method which sort polygon in polygon_list using their y coordinate,
        used to find a polygon faster than check all the polygon_list.
        This method set the polygon_coordinate attribute and must be called 
        after for every new tesselation.
        
        Returns
        -------
        None.

        """

        for poly in self.polygon_list:
            # For each point in the polygon
            for j in range(poly.count()):
                
                # To avoid to to go past the list
                if (0 <= poly.at(j).y() <= SettingsWindow.get_max_screen_size()[1] + 1): 
                
                    # Polygon added in list at the indice : point.y coordinate    
                    self.polygon_coordinate[int(poly.at(j).y())].append(poly)
                    
                    
    def generate_non_modifiable_point(self):
        """
        Method which set the fixed_point attribute by saving all initial points.
        Initial points are the first n point of every polygon before their
        first modification.
        This method must be called before the first modification on tessellation

        Returns
        -------
        None.

        """
        self.fixed_points.clear()
        for poly in self.polygon_list:
            
            for i in range(0,poly.count()):
                
                # Saved each point of every polygon in the list
                self.fixed_points.append(poly.at(i))
                
    def can_move(self,point):
        """
        

        Parameters
        ----------
        point : QPOINT
            Point that you want to now if it's allow to move.

        Returns
        -------
        bool
            if True : the point in paramater is allow to move
            if False : the point in paramater isn't allow to move.

        """
        
        # If the list doesn't contain the point it can move 
        if(self.fixed_points.count(point) != 0):
            
                return False
            
        return True
    
    def add_point_to_all(self, point, indice_in_poly, indice_of_poly):
        """
        Method which add the point in param at the indice indice_in_poly
        in all the polygon in polygon_list.
        This method calculate the shift to put the point at the right 
        coordinate in the tessellation.

        Parameters
        ----------
        point : QPOINT
            Point to add in the polygons.
        indice_in_poly : INT
            indice of the point to add in the polygons.
        indice_of_poly : INT
            indice of the polygon where the point were added first,
            to calculate the shift for each point to add in the polygons.

        Returns
        -------
        None.

        """
        
        # Vector used to put the points in each polygon 
        vector = Vector(self.polygon_list[indice_of_poly].at(indice_in_poly - 1), point)  
        
        for j in range(0,len(self.polygon_list)):
            
            # Calculate point's coordinate for each polygon
            point = QtCore.QPoint(vector.get_vector()[0] + self.polygon_list[j].at(indice_in_poly - 1).x(),
                                  vector.get_vector()[1] + self.polygon_list[j].at(indice_in_poly - 1).y())
           
            self.polygon_list[j].insert(indice_in_poly,point)
           
            # If the user want to add central symmetry to the tesselation
            if (self.central_symmetry):
               
                # Calculation indice of the symmetry point to add
                symmetry_indice = ((self.polygon_list[j].count() - 1)//2 + indice_in_poly) % (self.polygon_list[j].count() - 1)
               
                
                if indice_in_poly < (self.polygon_list[j].count() - 1)//2:
                    symmetry_indice +=1
                
                # To avoid to put a point at the indice 0
                if indice_in_poly == (self.polygon_list[j].count() - 1)//2:
                    symmetry_indice = self.polygon_list[j].count()
                   
                # Calculate coordinate of the symmetry point
                sypoint = self.central_symmetry.calculate_central_symmetry(point, j)
              
                self.polygon_list[j].insert(symmetry_indice,sypoint)
               
           
            elif (self.axial_symmetry):
               
               symmetry_indice = ((self.polygon_list[j].count() - 1)//2 + indice_in_poly) % (self.polygon_list[j].count() - 1)
               
               if indice_in_poly < (self.polygon_list[j].count() - 1)//2:
                   symmetry_indice +=1
               
               if indice_in_poly == (self.polygon_list[j].count() - 1)//2:
                   symmetry_indice = self.polygon_list[j].count()
                   
               sympoint = self.axial_symmetry.calculate_axial_symmetry(point, j)
              
               self.polygon_list[j].insert(symmetry_indice,sympoint)
               self.axial_symmetry.set_symmetry_indice(symmetry_indice)
                  

    def modify_point_in_all(self, new_point, indice_in_poly, indice_of_poly):
        """
        Method which move the point at the indice indice_in_poly
        in all the polygon in polygon_list.
        This method calculate the shift to put the point at the right 
        coordinate in the tessellation. 

        Parameters
        ----------
        new_point : QPOINT
            point to put in the polygons.
        indice_in_poly : INT
            indice of the point to move in the polygons.
        indice_of_poly : INT
            indice of the polygon where the point were moved first,
            to calculate the shift for each point to move in the polygons.

        Returns
        -------
        None.

        """
        
        # Vector used to move the points in each polygon 
        vector = Vector(self.polygon_list[indice_of_poly].at(indice_in_poly - 1), new_point)  
        
        for j in range(0,len(self.polygon_list)):
            
            # Calculate point's coordinate for each polygon
            point = QtCore.QPoint(vector.get_vector()[0] + self.polygon_list[j].at(indice_in_poly - 1).x(),
                                   vector.get_vector()[1] + self.polygon_list[j].at(indice_in_poly - 1).y())
            
            # If the user want to add central symmetry to the tesselation
            if (self.central_symmetry):
                
                # Calculate coordinate of the symmetry point
                sypoint = self.central_symmetry.calculate_central_symmetry(point, j)
                
                # Calculation indice of the symmetry point to move
                symmetry_indice = ((self.polygon_list[j].count() - 2) // 2 + indice_in_poly) % (self.polygon_list[j].count() - 2)
                
                # If point to move is in the first half [0: (cout - 2) // 2]
                if indice_in_poly < (self.polygon_list[j].count() - 2) // 2:
                    
                    # We adjust the symmetry_indice
                    symmetry_indice +=1
                
                # If point to move is at the middle indice : (count - 2) // 2
                if indice_in_poly == (self.polygon_list[j].count() - 2) // 2:
                    symmetry_indice = self.polygon_list[j].count() - 1
                
                indice = indice_in_poly 
                
                # If a point is added "after" his symmetry we adjust its indice
                if(symmetry_indice < indice_in_poly and self.added_point):
                    indice += 1
                    
                # If no point added 
                if(symmetry_indice < indice_in_poly and not self.added_point):
                    symmetry_indice -= 1    
                    
                    
                self.polygon_list[j].replace(indice,point)
                
                self.polygon_list[j].replace(symmetry_indice,sypoint)
                
             
            elif (self.axial_symmetry):
                sympoint = self.axial_symmetry.calculate_axial_symmetry(point, j)
                
                symmetry_indice = self.axial_symmetry.get_symmetry_indice()
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
                self.polygon_list[j].replace(symmetry_indice,sympoint)
                
            else:
                self.polygon_list[j].replace(indice_in_poly,point)  
            

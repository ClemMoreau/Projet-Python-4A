from model.polygonInformation import PolygonInformation
from model.vector import Vector

from controller.saveController import SaveController

from view.saveWindow import SaveWindow
from view.loadWindow import LoadWindow

from PyQt5 import QtWidgets, QtGui, QtCore, Qt

# Margin used to decide if a point is near a line or not
MARGIN_ALLOWED = 2

# Color allowed to draw polygons
COLOR_ALLOWED = ["white", "red", "green", "blue",
                 "black", "darkRed", "darkGreen", "darkBlue",
                 "cyan", "magenta", "yellow", "gray",
                 "darkCyan", "darkMagenta", "darkYellow", "darkGray", "lightGray",
                 'rainbow']

class Tessellation(QtWidgets.QWidget):
    
        # =============== #
        #   CONSTRUCTOR   #
        # =============== #
    
    def __init__(self, polygon_type, nb_polygon_per_line, central_symmetry = False, color = "cyan"):
        """
        Constructor of the Tessellation class

        Parameters
        ----------
        polygon_type : STRING
            polygon type give to the PolygonInformation attribute.
        nb_polygon_per_line : INT
            number of polygon per line on the screen.
        central_symmetry : BOOL, optional
            if user want to add central symmetry in the tesselation.
            The default is False.
        color : TYPE, optional
            color to draw polygons. 
            The default is "cyan".

        Returns
        -------
        None.

        """
        
        # Constructorof the QWidget class
        super().__init__()
        
        self.polygon_information = PolygonInformation(polygon_type, nb_polygon_per_line, central_symmetry)
        
        self.point_to_move = False
        self.indice_in_poly = -1
        self.indice_of_poly = -1
        
        if(color in COLOR_ALLOWED):
            self.color = color
        
        # To be abble to get the cursor position at any time
        self.setMouseTracking(True)
        
        # Allow user to save his tessellation
        SaveWindow.set_save_widget(SaveController())
        SaveWindow.save_widget.show()
        
        # =========== #
        #   GETTERS   #
        # =========== #

    def get_polygon_information(self):
        """
        Getter of the polygon_information attribute

        Returns
        -------
        POLYGONINFORMATION
            represent all the operation and data of the polygons.

        """
        
        return self.polygon_information
    
    def get_point_to_move(self):
        """
        Getter of the point_to_move attribute

        Returns
        -------
        BOOL

        """
        return self.point_to_move
    
    def get_indice_in_poly(self):
        """
        Getter of the indice_in_poly attribute

        Returns
        -------
        INT
            Indice of the point to modify in polygons.

        """
        return self.indice_in_poly
    
    def get_indice_of_poly(self):
        """
        Getter of the indice_of_poly attribute

        Returns
        -------
        INT
            indice of the polygon to modify.

        """
        
        return self.indice_of_poly
    
    def get_color(self):
        """
        Getter of the color attribute

        Returns
        -------
        STRING
            color of the polygons drawed on the tessellation.

        """
        
        return self.color
    
        # =========== #
        #   SETTERS   #
        # =========== #
    
    def set_polygon_information(self, polygon_information):
        """
        Setter of the polygon_information

        Parameters
        ----------
        polygon_information : POLYGONINFORMATION
            new PolygonInformation 
            representing all the operation and data of the new polygons.

        Returns
        -------
        None.

        """
        
        if(polygon_information):
            self.polygon_information = polygon_information
            
    def set_point_to_move(self, boolean):
        """
        Setter of the point_to_move attribute

        Parameters
        ----------
        boolean : BOOL
            true if a point need to be moved,
            false else.
        Returns
        -------
        None.

        """
        
        self.point_to_move = boolean
        
    def set_indice_in_poly(self, indice):
        """
        Setter of the indice_in_poly attribute

        Parameters
        ----------
        indice : INT
            new indice of the point to modify in polygons.

        Returns
        -------
        None.

        """
        
        if(indice >= 0):
            self.indice_in_poly = indice
            
    def set_indice_of_poly(self, indice):
        """
        Setter of the indice_of_poly attribute

        Parameters
        ----------
        indice : INT
            new indice of the polygon to modify.

        Returns
        -------
        None.

        """
        
        if(indice >= 0):
            self.indice_of_poly = indice
            
    def set_color(self, color):
        """
        Setter of the color attribute

        Parameters
        ----------
        color : STRING
            new color to draw polygons.

        Returns
        -------
        None.

        """
        
        if(color in COLOR_ALLOWED):
            self.color = color
            
        # =========== #
        #   METHODS   #
        # =========== #

    def paintEvent(self, event):
        """
        Method which draw on the tesselation.
        This method musn't call manualy

        Parameters
        ----------
        event : QPAINTEVENT
            any QPaintEvent on the widget
            (resize, click...).

        Returns
        -------
        None.

        """
        
        # Call the painter of the widget
        painter = QtGui.QPainter(self)
        
        indice = 0
        
        for poly in self.polygon_information.get_polygon_list():
            
            if(self.color == 'rainbow'):
                painter.setBrush(Qt.QColor(COLOR_ALLOWED[indice % (len(COLOR_ALLOWED) - 1)]))
                indice += 1
            else:
                painter.setBrush(Qt.QColor(self.color))
            
            painter.drawPolygon(poly)
       
    def mouseReleaseEvent(self, event):
        """
        Method called when the user release the mouse over the widget

        Parameters
        ----------
        event : QMOUSEEVENT
            event cause by the release of the mouse.

        Returns
        -------
        None.

        """
        
        if(self.point_to_move):
           
            # Used to call PaintEvent()
            self.update()
            
            # If the user release the mouse, there is no more point to move 
            self.point_to_move = False
            
            # To know at the next mouse press if a point is added
            self.polygon_information.added_point = False
        
    def mouseMoveEvent(self, event):
        """
        Method called when the user move the mouse over the widget

        Parameters
        ----------
        event : QMOUSEEVENT
            event cause by the move of the mouse.

        Returns
        -------
        None.

        """
        
        # Change the cursor appearence
        if(not self.cursor_near_point(event.pos())):
            QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        
        # If points need to be moved
        if(self.point_to_move): 
            
            # We moved the points with the position of the event in param
            self.polygon_information.modify_point_in_all(event.pos(), self.indice_in_poly, self.indice_of_poly)
            
        # Used to call PaintEvent()
        self.update()
       
    def mousePressEvent(self, event):

            search_area = self.find_search_area(event.pos())
            
            for j in range(0,len(search_area)):
                for i in range (0,search_area[j].count()):
                    
                    distance = Vector(search_area[j].at(i % search_area[j].count()), event.pos())
                    
                    if(distance.vector_length() < 10):
                        
                        if(self.polygon_information.can_move(search_area[j].at(i % search_area[j].count()))):
                        
                            self.indice_in_poly = i
                            self.indice_of_poly = self.get_corresponding_index(search_area[j])
                            
                            if(self.indice_of_poly != None):
                                
                                self.point_to_move = True
                                self.polygon_information.modify_point_in_all(event.pos(), self.indice_in_poly, self.indice_of_poly)
                                self.polygon_information.added_point = False 
                        return
                        
                       
                    vector = Vector(search_area[j].at(i % search_area[j].count()),
                                    search_area[j].at((i + 1) % search_area[j].count()))
                    distance_to_line = vector.distance_point_line(event.pos())
                    
                    if (type(distance_to_line) != type(None)):
                        if (distance_to_line[0] <= MARGIN_ALLOWED and
                            distance_to_line[0] >= -MARGIN_ALLOWED and
                            distance_to_line[1] <= MARGIN_ALLOWED and
                            distance_to_line[1] >= -MARGIN_ALLOWED):
                            
                            self.indice_in_poly = i + 1
                            self.indice_of_poly = self.get_corresponding_index(search_area[j])
                            
                            if(self.indice_of_poly != None):
                                
                                self.point_to_move = True 
                                self.polygon_information.add_point_to_all(event.pos(), self.indice_in_poly, self.indice_of_poly)
                                
                                self.polygon_information.added_point = True
                            
                            return
            
    def closeEvent(self, event):
        
       SaveWindow.save_widget.close()
       LoadWindow.load_widget.close()
    
        #a dégager dans polyinfo?
    
    def find_search_area(self, point):
        
        search_area = []
        indice = -1
        
        while(0 <= int(point.y() + indice) < len (self.polygon_information.get_polygon_coordinate()) and len(self.polygon_information.get_polygon_coordinate()[int(point.y() + indice)]) == 0):
            indice -= 1
            
        for i in range(0,len(self.polygon_information.get_polygon_coordinate()[int(point.y() + indice)])):
            search_area.append(self.polygon_information.get_polygon_coordinate()[int(point.y() + indice)][i])
                
        indice = 0
        
        while(0 <= int(point.y() + indice) < len(self.polygon_information.get_polygon_coordinate()) and 
              len(self.polygon_information.get_polygon_coordinate()[int(point.y() + indice)]) == 0):
            indice += 1    
            
        if(0 <= int(point.y() + indice) < len(self.polygon_information.get_polygon_coordinate())):
            for i in range(0,len(self.polygon_information.get_polygon_coordinate()[int(point.y() + indice)])):
                search_area.append(self.polygon_information.get_polygon_coordinate()[int(point.y() + indice)][i])
            
        return search_area
    
    def get_corresponding_index(self, poly):
        
        for i in range(0,len(self.polygon_information.get_polygon_list())):
            if (self.polygon_information.get_polygon_list()[i] is poly):
                return i
        return None

    
    def cursor_near_point(self, point):
        
        search_area = self.find_search_area(point)
        
        for j in range(0,len(search_area)):
            for i in range (0,search_area[j].count()):
                
                distance = Vector(search_area[j].at(i % search_area[j].count()), point).vector_length()
                
                if distance < 10 :
                    QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    if(not self.polygon_information.can_move(search_area[j].at(i % search_area[j].count()))):
                       QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                    return True
        return False

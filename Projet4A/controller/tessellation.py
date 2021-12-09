from model.polygonInformation import PolygonInformation
from model.vector import Vector

from controller.saveController import SaveController

from view.saveWindow import SaveWindow
from view.loadWindow import LoadWindow

from PyQt5 import QtWidgets, QtGui, QtCore, Qt


MARGIN_ALLOWED = 2
COLOR_ALLOWED = ["white", "red", "green", "blue",
                 "black", "darkRed", "darkGreen", "darkBlue",
                 "cyan", "magenta", "yellow", "gray",
                 "darkCyan", "darkMagenta", "darkYellow", "darkGray", "lightGray",
                 'rainbow']

class Tessellation(QtWidgets.QWidget):
    
    # =============== #
    #   CONSTRUCTOR   #
    # =============== #
    
    def __init__(self, polygon_type, nb_polygon_per_line, central_symmetry, color = "cyan"):
        
        super().__init__()
        
        self.polygon_information = PolygonInformation(polygon_type, nb_polygon_per_line, central_symmetry)
        
        self.point_to_move = False
        self.indice_in_poly = -1
        self.indice_of_poly = -1
        
        if(color in COLOR_ALLOWED):
            self.color = color
        
        
        self.setMouseTracking(True)
        
        SaveWindow.set_save_widget(SaveController())
        SaveWindow.save_widget.show()
    
    # =========== #
    #   GETTERS   #
    # =========== #

    def get_polygon_information(self):
        return self.polygon_information
    
    def get_point_to_move(self):
        return self.point_to_move
    
    def get_indice_in_poly(self):
        return self.indice_in_poly
    
    def get_indice_of_poly(self):
        return self.indice_of_poly
    
    def get_color(self):
        return self.color
    
    # =========== #
    #   SETTERS   #
    # =========== #
    
    def set_polygon_information(self, polygon_information):
        if(polygon_information):
            self.polygon_information = polygon_information
            
    def set_point_to_move(self, boolean):
        self.point_to_move = boolean
        
    def set_indice_in_poly(self, indice):
        if(indice >= 0):
            self.indice_in_poly = indice
            
    def set_indice_of_poly(self, indice):
        if(indice >= 0):
            self.indice_of_poly = indice
            
    def set_color(self, color):
        if(color in COLOR_ALLOWED):
            self.color = color
            
    # =========== #
    #   METHODS   #
    # =========== #

    def paintEvent(self, event):
        
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
        
        if(self.point_to_move):
           self.update()
           self.point_to_move = False
           self.polygon_information.added_point = False
        
    def mouseMoveEvent(self, event):

        if(not self.cursor_near_point(event.pos())):
            QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                
        if(self.point_to_move): 
            self.polygon_information.modify_point_in_all(event.pos(), self.indice_in_poly, self.indice_of_poly)
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

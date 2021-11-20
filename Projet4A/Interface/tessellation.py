import numpy as np, math, saver as save, loader as load
from PyQt5 import QtWidgets, QtGui, QtCore, Qt

#déplacer à l'intérieur de la classe?
MARGIN_ALLOWED = 2

class Tessellation(QtWidgets.QWidget):
    """VOIR POUR BOUGER LA CREATION POLYGON (OBJ) ICI"""
    def __init__(self, polygon):
        super().__init__()
        
        self.polygon = polygon
        
        self.typeofPolygon = str(type(polygon))
        
        self.polygon_list = self.polygon.generate_poly()    
        
        
        self.polygon_coordinate = [[] for i in range(polygon.size[1] + 1)]
        self.generate_coordinates()
        
        self.fixed_points = []
        self.generate_non_modifiable_point()
            
        self.point_to_move = False
        
        self.setMouseTracking(True)
        self.set_graphic_interface()

#==============================================================================    
#   METHODS
#==============================================================================
    


    def paintEvent(self, event):
        
        painter = QtGui.QPainter(self)
        
        painter.setBrush(Qt.QColor("cyan"))
        for poly in self.polygon_list:
            painter.drawPolygon(poly)
       
    def mouseReleaseEvent(self, event): # evenement mouseRelease
        if(self.point_to_move):  
           self.update()
           self.point_to_move = False
               
        
    def mouseMoveEvent(self, event):
       
        if(not self.cursor_near_point(event.pos())):
            QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        
        if(self.point_to_move): 
            self.modify_point_in_all(event.pos())
        self.update()
       
    def mousePressEvent(self, event): # evenement mousePress
        self.last_point_added = event.pos()
        search_area = self.find_search_area(event.pos())
        
        for j in range(0,len(search_area)):
            for i in range (0,search_area[j].count()):
                
                distance = self.vector_length(self.line_to_vector(search_area[j].at(i % search_area[j].count()), event.pos()))
                
                if(distance < 10):
                    
                    if(self.can_move(search_area[j].at(i % search_area[j].count()))):
                    
                        self.indice_in_poly = i
                        self.indice_of_poly = self.get_corresponding_index(search_area[j])
                        if(self.indice_of_poly != None):
                            
                            self.point_to_move = True
                            self.modify_point_in_all(event.pos()) 
                    return
                    
                   
                distance_to_line = self.distance_point_line(search_area[j].at(i % search_area[j].count()),
                                                            search_area[j].at((i + 1) % search_area[j].count()),
                                                            event.pos())
                
                if (type(distance_to_line) != type(None)):
                    
                        if (distance_to_line[0] <= MARGIN_ALLOWED and
                            distance_to_line[0] >= -MARGIN_ALLOWED and
                            distance_to_line[1] <= MARGIN_ALLOWED and
                            distance_to_line[1] >= -MARGIN_ALLOWED):
                            
                            self.indice_in_poly = i + 1
                            self.indice_of_poly = self.get_corresponding_index(search_area[j])
                            if(self.indice_of_poly != None):
                                
                                self.point_to_move = True 
                                self.add_point_to_all(event.pos())
                            
                            return
                            
                            
    def distance_point_line(self, line_start_point, line_end_point, point):
        
        #check if the point is between segment terminals 
        X = (min(line_end_point.x(), line_start_point.x()),
             max(line_end_point.x(), line_start_point.x()))
        Y = (min(line_end_point.y(), line_start_point.y()),
             max(line_end_point.y(), line_start_point.y()))
        
        if (X[0] == X[1] or Y[0] == Y[1]):
            margin = 5
        else:
            margin = 0
            
        if(X[0] - margin < point.x() < X[1] + margin and 
           Y[0] - margin < point.y() < Y[1] + margin):
        
            line_vector = np.array(self.line_to_vector(line_start_point, line_end_point))
            
            vector_to_projeted = np.array(self.line_to_vector(line_start_point, point))
            
            projected_vector = (np.dot(vector_to_projeted, line_vector) / np.dot(line_vector, line_vector))*line_vector
            
            return (vector_to_projeted - projected_vector)
            
    def add_point_to_all(self, point):
        
        vector = self.line_to_vector(self.polygon_list[self.indice_of_poly].at(self.indice_in_poly - 1), point)  
        
        for j in range(0,len(self.polygon_list) - 1):
            
           point = QtCore.QPoint(vector[0] + self.polygon_list[j].at(self.indice_in_poly - 1).x(),
                                  vector[1] + self.polygon_list[j].at(self.indice_in_poly - 1).y())
           
           self.polygon_list[j].insert(self.indice_in_poly,point)
           
           if (self.typeofPolygon == "+<class 'square.Square'>"):
               point = QtCore.QPointF(vector[0] + self.polygon_list[j].at((self.indice_in_poly + (self.polygon_list[j].count() + 1)/2) % (self.polygon_list[j].count())).x(),
                                      vector[1] + self.polygon_list[j].at((self.indice_in_poly + (self.polygon_list[j].count() + 1)/2) % (self.polygon_list[j].count())).y())
               self.polygon_list[j].insert((self.indice_in_poly + (self.polygon_list[j].count() + 1)/2) % (self.polygon_list[j].count()),point)
        

    def modify_point_in_all(self, new_point):
        
        vector = self.line_to_vector(self.polygon_list[self.indice_of_poly].at(self.indice_in_poly - 1), new_point)  

        for j in range(0,len(self.polygon_list) - 1):
            
            point = QtCore.QPoint(vector[0] + self.polygon_list[j].at(self.indice_in_poly - 1).x(),
                                   vector[1] + self.polygon_list[j].at(self.indice_in_poly - 1).y())
            
            self.polygon_list[j].replace(self.indice_in_poly,point)
            
            if (self.typeofPolygon == "+<class 'square.Square'>"):
                #C'est ici que ça bug l'indice est pas bon
                point = QtCore.QPointF(vector[0] + self.polygon_list[j].at((self.indice_in_poly + (self.polygon_list[j].count() + 1)/2) % (self.polygon_list[j].count())).x(),
                                       vector[1] + self.polygon_list[j].at((self.indice_in_poly + (self.polygon_list[j].count() + 1)/2) % (self.polygon_list[j].count())).y())
                
                self.polygon_list[j].replace((self.indice_in_poly + (self.polygon_list[j].count() + 1)/2) % (self.polygon_list[j].count()),point)
            
    def line_to_vector(self, line_start_point, line_end_point):
        
        return (line_end_point.x() - line_start_point.x(),
                line_end_point.y() - line_start_point.y(),
                )
    
    def generate_coordinates(self):
        
        for poly in self.polygon_list:
            for j in range(poly.count()):
                if (0 <= poly.at(j).y() <= self.polygon.size[1] + 1): 
                    self.polygon_coordinate[int(poly.at(j).y())].append(poly)
                    
    def generate_non_modifiable_point(self):
        
        for poly in self.polygon_list:
            for i in range(0,poly.count()):
                self.fixed_points.append(poly.at(i))
            
        #a modifier pour prendre plus de ligne si pas dans la zone
    def find_search_area(self, point):
        
        search_area = []
        indice = -1
        
        while(0 <= int(point.y() + indice) < len (self.polygon_coordinate) and len(self.polygon_coordinate[int(point.y() + indice)]) == 0):
            indice -= 1
            
        for i in range(0,len(self.polygon_coordinate[int(point.y() + indice)])):
            search_area.append(self.polygon_coordinate[int(point.y() + indice)][i])
                
        indice = 0
        
        while(0 <= int(point.y() + indice) < len(self.polygon_coordinate) and 
              len(self.polygon_coordinate[int(point.y() + indice)]) == 0):
            indice += 1    
            
        if(0 <= int(point.y() + indice) < len(self.polygon_coordinate)):
            for i in range(0,len(self.polygon_coordinate[int(point.y() + indice)])):
                search_area.append(self.polygon_coordinate[int(point.y() + indice)][i])
            
        return search_area
    
    def get_corresponding_index(self, poly):
        
        for i in range(0,len(self.polygon_list)):
            if (self.polygon_list[i] is poly):
                return i
        return None
    
    def vector_length(self, vector):
        return math.sqrt(vector[0]**2 + vector[1]**2)
    
    def can_move(self,point):
    
        if(self.fixed_points.count(point) != 0):
                return False
        return True
    
    def cursor_near_point(self, point):
        
        search_area = self.find_search_area(point)
        
        for j in range(0,len(search_area)):
            for i in range (0,search_area[j].count()):
                
                distance = self.vector_length(self.line_to_vector(search_area[j].at(i % search_area[j].count()), point))

                if distance < 10 :
                    QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    if(not self.can_move(search_area[j].at(i % search_area[j].count()))):
                       QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                    return True
        return False
    
    def set_graphic_interface(self):
        
        self.menu = QtWidgets.QMenuBar(self)
        self.menu.addSeparator()
        self.save = self.menu.addAction('Save')
        self.save.triggered.connect(self.save_tesselation)
        self.load = self.menu.addAction('Load')
        self.load.triggered.connect(self.load_tesselation)
        
    def save_tesselation(self):
        
        saving = save.Saver(self.polygon_list, 'C:/Users/cleme/OneDrive/Bureau/testPython.txt')
        saving.save_object()
        
    def load_tesselation(self):
        
        loading = load.Loader('C:/Users/cleme/OneDrive/Bureau/testPython.txt')
        loading.load_object()    
        
        self.polygon_list.clear()        
        self.polygon_list = loading.get_object_loaded()
        self.generate_non_modifiable_point()
        self.generate_coordinates()
        self.update()                          
       
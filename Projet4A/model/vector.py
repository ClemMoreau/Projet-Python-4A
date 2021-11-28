import math
import numpy as np

from PyQt5 import QtCore


class Vector(object):
    
    #==========================================================================
    #   CONSTRUCTOR
    #==========================================================================
    
    def __init__(self, start_point, end_point):
        
        self.start_point = start_point
        
        self.end_point = end_point
        
        self.vector = self.line_to_vector(start_point, end_point)
        
    #==========================================================================
    #   GETTERS
    #==========================================================================
    
    def get_start_point(self):
        return self.start_point
    
    def get_end_point(self):
        return self.end_point
    
    def get_vector(self):
        return self.vector
    
    #==========================================================================
    #   SETTERS
    #==========================================================================
    
    def set_start_point(self, point):
        
        if(point):
            self.start_point = point
            self.vector = self.line_to_vector(self.start_point, self.end_point)
            
    def set_end_point(self, point):
        if(point):
            self.end_point= point
            self.vector = self.line_to_vector(self.start_point, self.end_point)
        
    def set_vector(self, vector):
        if(vector):
            self.vector = self.line_to_vector(QtCore.QPoint(0,0), QtCore.QPoint(vector[0],vector[1]))
            
    #==========================================================================
    #   METHODS
    #==========================================================================        
    
    def line_to_vector(self, line_start_point, line_end_point):
        
        return (line_end_point.x() - line_start_point.x(),
                line_end_point.y() - line_start_point.y(),
                )
    
    def vector_length(self):
        return math.sqrt(self.vector[0]**2 + self.vector[1]**2)

    def distance_point_line(self, point):
        
        #check if the point is between segment terminals 
        X = (min(self.end_point.x(), self.start_point.x()),
             max(self.end_point.x(), self.start_point.x()))
        Y = (min(self.end_point.y(), self.start_point.y()),
             max(self.end_point.y(), self.start_point.y()))
        
        if (X[0] == X[1] or Y[0] == Y[1]):
            margin = 5
        else:
            margin = 0
            
        if(X[0] - margin < point.x() < X[1] + margin and 
           Y[0] - margin < point.y() < Y[1] + margin):
        
            line_vector = np.array(self.line_to_vector(self.start_point, self.end_point))
            
            vector_to_projeted = np.array(self.line_to_vector(self.start_point, point))
            
            projected_vector = (np.dot(vector_to_projeted, line_vector) / np.dot(line_vector, line_vector))*line_vector
            
            return (vector_to_projeted - projected_vector)

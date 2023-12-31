'''
Team Tutorial #4: Point class
'''

import math

class Point:
    def __init__(self, x, y):
        '''
        Constructor for the Point class

        Input:
            x: (float) x-coordinate
            y: (float) y-coordinate
        '''

        self.x = x
        self.y = y

    def distance_to_origin(self):
        '''
        Calculate the distance to the origin

        Returns: distance (float)

        '''
        return math.sqrt(self.x**2 + self.y**2)

    def to_polar(self):
        '''
        Compute the polar coordinates

        Returns: radial coordinate, angular
          coordinate in degrees (tuple)

        '''
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.degrees(math.atan(self.y/self.x))
        return r, theta

    def distance(self, other):
        '''
        Calculate the distance between two points

        Input:
            other: (Point) the other point

        Returns: distance (float)
        '''
        x1 = self.x 
        y1 = self.y
        x2 = other.x
        y2 = other.y

        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return d

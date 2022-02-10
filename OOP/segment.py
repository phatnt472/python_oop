from math import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'x: {self.x}\ny: {self.y}\n'
class LineSegment:
    def __init__(self,start_point = Point(0,0),end_point = Point(1,1)):
        self.start_point = start_point
        self.end_point = end_point
    def slope(self):
        return (self.end_point.y - self.start_point.y)/(self.end_point.x - self.start_point.x)
    
    def length(self):
        return sqrt((self.end_point.x-self.start_point.x)**2 + (self.end_point.y-self.start_point.y)**2)
    def __str__(self):
        return str(self.start_point) + str(self.end_point)

segment = LineSegment(Point(1,1),Point(3,2))
print(segment)
print(f'Slope: {segment.slope()}')
print(f'Length: {segment.length()}')


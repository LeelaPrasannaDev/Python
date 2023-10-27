'''
. Write a Python program to create a class representing a Circle.
Include methods to calculate its area and perimeter.
'''

import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2* math.pi*self.radius

a = Circle(30)
print('Area of circle = ',a.area())
print('Perimeter of circle = ',a.perimeter())

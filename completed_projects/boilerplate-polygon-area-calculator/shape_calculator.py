import math
class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  def get_area(self):
    return self.height*self.width
  def get_perimeter(self):
    return 2*self.height+2*self.width
  def get_diagonal(self):
    return math.sqrt(self.width**2+self.height**2)



class Square:

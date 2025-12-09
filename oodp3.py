"""Rectangle Area & Perimeter
Create a class Rectangle with attributes: length and breadth.

Write methods to calculate area and perimeter.

Take length and breadth from user and print area & perimeter."""
class Rectangle:
    def __init__(self,lenght,breadth):
        self.length = lenght
        self.breadth = breadth
    def area(self):
        print("the area of the rectangle is ", self.length * self.breadth)
    def perimeter(self):
        print("the perimeter of the rectangle is ", self.length * self.breadth)
r1 = Rectangle(10,20)
r1.area()
r1.perimeter()

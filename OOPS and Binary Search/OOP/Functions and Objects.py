"""Create a class Triangle Having 3 sides as attributes (side1, side2, side 3).

Create a constructor to initialize the sides in realtime on object creation.

Create 2 functions calculate_area and calculate_perimeter

calculate_area functions returns the area of the triangle ( side1 * side2 * side3)

calculate_perimeter functions returns the perimeter of the triangle (side1+side2+side3)."""


class Triangle:

    def __init__(self, side1, side2, side3):    # constructor
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):   # function
        return self.side1 * self.side2 * self.side3

    def calculate_perimeter(self):  # function
        return self.side1 + self.side2 + self.side3


triangle_obj = Triangle(3, 4, 6)    # object
print(triangle_obj.calculate_area())
per = triangle_obj.calculate_perimeter()
print(per)

# Constructor: __init__(self, side1, side2, side3)
# Functions: calculate_area(self) and calculate_perimeter(self)
# Objects: triangle_obj (an instance of the Triangle class)

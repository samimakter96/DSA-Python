"""Create a class named 'Shape' with a method to printShape "This is shape".

 Then create two other classes named 'Rectangle', 'Circle' inheriting the Shape class, both having a method to print
 "This is rectangle" and "This is circle" respectively.

 Create a child class 'Square' of 'rectangle' having a method to printSquare "Square is a rectangle".
 Now call the method of 'Shape' and 'Rectangle' class by the object of 'Square' class.
"""


class Shape:    # parent class

    def printShape(self):
        print("This is shape")


class Rectangle(Shape):  # child class

    def print(self):
        print("This is rectangle")


class Circle(Shape):    # child class

    def print(self):
        print("This is circle")


class Square(Rectangle):    # grandchild class

    def printSquare(self):
        print("Square is a rectangle")


x = Square()
x.printSquare()
x.printShape()
x.print()

y = Circle()
y.print()
y.printShape()
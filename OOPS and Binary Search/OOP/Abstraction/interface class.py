from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def show(self):
        pass


class Square(Shape):
    def show(self):
        print("Square has 4 sides")


class Circle(Shape):
    def show(self):
        print("Circle has circle shape")


s = Square()
s.show()

c = Circle()
c.show()
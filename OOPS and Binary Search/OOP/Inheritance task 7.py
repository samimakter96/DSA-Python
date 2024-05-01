# Destructors --> Destructors are called when an objects gets destroyed
"""destructors are an important feature of Python and can help to ensure that objects are properly cleaned up
and resources are not wasted. They are easy to use and can be useful for enforcing encapsulation and other principles of
object-oriented design."""


class Employee:
    # Initializing
    def __init__(self):
        print("Employee created")

    # Deleting (calling Destructor)
    def __del__(self):
        print("Destructors called, Employee deleted")


obj = Employee()
del obj


""" Create a class "PARENT" with a method print that prints "this is a parent class" and its Child class "CHILD" 
with a method print that prints "this is a child class". Now, create an object for each of the class and call

1 - method of parent class by object of parent class

2 - method of child class by object of child class

3 - method of parent class by object of child class
"""


class PARENT:

    def print(self):
        print("this is a parent class")


class CHILD(PARENT):

    def print(self):
        print("this is a child class")

        super().print()    # inheriting the properties of parent class using super(). function


def main():
    obj_parent = PARENT()
    obj_parent.print()

    obj_child = CHILD()
    obj_child.print()


main()
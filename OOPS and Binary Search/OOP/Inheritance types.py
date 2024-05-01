# Different types of python Inheritance

"""1. Single Inheritance: When a Child class inherits from only one parents class, it is called single inheritance"""

# parent class


class A:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

# Child class


class B(A):

    def __init__(self, name):
        self.sName = name

        super().__init__("Rahul")   # inheriting the properties of parent class using super() function

    def display(self):
        print(self.sName)


obj = B("Samim")
obj.get_name()
obj.display()

"""2. Multiple inheritances: When a Child class inherits from a multiple Parent classes, it is called Multiple 
inheritances """


class Father:

    def __init__(self):
        self.str1 = "Parents1"
        print("Father class")


class Mother:

    def __init__(self):
        self.str2 = "Parents2"
        print("Mother class")


class Child(Father, Mother):

    def __init__(self):

        # Calling constractor of Father and Mother classes
        Father.__init__(self)
        Mother.__init__(self)
        print("Child")

    def print_strs(self):
        print(self.str1, self.str2)


obj = Child()
obj.print_strs()


"""3. Multilevel inheritance: When we have Child and grandchild relationship. This means that a Child class will 
inherit from its parents class. which in turn is inheriting from its parents class"""


class Base:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# Inherited or Sub Class (Note Base/Parent class in bracket)
class Child(Base):

    # Constractor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def get_age(self):
        return self.age


class Grandchild(Child):

    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def get_address(self):
        return self.address


g = Grandchild("Samim", 20, "West Bengal")
print(g.get_name(), g.get_age(), g.get_address())
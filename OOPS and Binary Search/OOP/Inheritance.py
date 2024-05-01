# Basic syntax of inheritance:

# class BaseClass:
#     {Body}
# class DerivedClass(BaseClass):
#     {Body}

# Creating a Parent Class
# --> a parent class is a class whose properties are inherited by the child class

class Person:

    # Constractor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # print name and id
    def display(self):
        print(self.name, self.id)


emp = Person("Satyam", 102)  # emp an object of Person
emp.display()

# Creating a Child Class:


class Student(Person):

    def Print(self):
        print("Student is a Child class")


student_details = Student("Ankit", 103)

# calling parent class function
student_details.display()

# calling child class function
student_details.Print()

# Example:


class Person:   # Parent Class

    # Constractor
    def __init__(self, name):
        self.name = name

    # To get name
    def get_name(self):
        return self.name

    # To check if the person is an employee
    def is_Employee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):  # Child Class

    # Here we return True
    def is_Employee(self):
        return True


emp = Person("Greek1")  # An object of Person
print(emp.get_name(), emp.is_Employee())

emp2 = Employee("Samim")    # An object of Employee
print(emp2.get_name(), emp.is_Employee())


# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)


# child class
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id_number)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()

""" super() --> return the object that represent the parent class. it's allow to access to the parents clas's methods
 and attributes in the child class """


# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

# child class


class Student(Person):

    def __init__(self, name, age):
        self.sName = name
        self.sAge = age

        # inheriting the properties of parent class
        super().__init__("Rahul", age)

    def display_info(self):
        print(self.sName, self.sAge)


obj = Student("Samim", 20)
obj.display()
obj.display_info()

"""Adding Properties"""


class Person:   # parent class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):   # child class

    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob

        super().__init__("Salman", age)

    def details(self):
        print(self.sName, self.sAge, self.dob)


obj = Student("Samim", 20, "5-9-2003")
obj.display()
obj.details()
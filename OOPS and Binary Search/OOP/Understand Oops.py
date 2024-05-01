# Define a Car class
class Car:

    # Class attributes
    wheels = 4

    # This is a special method called the constructor
    def __init__(self, color, model):

        # These are Instance attributes of the Car class
        self.color = color
        self.model = model
        self.is_engine_on = False  # By default, the engine is off

    # This is a method that makes the car start its engine
    def start_engine(self):
        if not self.is_engine_on:
            print(f"The {self.color} {self.model}'s engine is now running.")
            self.is_engine_on = True
        else:
            print("The engine is already running.")

    # This is a method that makes the car stop its engine
    def stop_engine(self):
        if self.is_engine_on:
            print(f"The {self.color} {self.model}'s engine is now turned off.")
            self.is_engine_on = False
        else:
            print("The engine is already off.")


# Creating two car objects based on the Car class
car1 = Car(color="red", model="Sedan")
car2 = Car(color="blue", model="SUV")

# Accessing attributes of the car objects
print(f"The {car1.color} {car1.model} is a {Car.wheels} wheels and a fantastic car.")
print(f"The {car2.color} {car2.model} is a {Car.wheels} wheels and a powerful SUV.")

# Using methods to start and stop the engines

# Starting the engine for the first time
car1.start_engine()  # Output: "The red Sedan's engine is now running."
# Trying to start the engine again
car1.start_engine()  # Output: "The engine is already running."

car2.start_engine()   # Output: "The blue SUV engine is now running."
car2.start_engine()   # Output: "The engine is already running."

car1.stop_engine()
car2.stop_engine()


"""Class attributes:
imagine you have a school and you want to keep track some information about all the students. the information like 
school name, school address, school contact no. this shared information all the students have same this is called class
attributes"""


"""Instance attributes:
Now, let's say you want to keep track of specific details for each individual students, like their name, age and grade.
these details are unique to each students this is called instance attributes."""


class School:
    # Class attribute
    school_name = "ABC School"
    school_address = "123 Main Street"
    contact_number = "555-1234"

    def __init__(self, student_name, student_age, student_grade):
        # Instance attributes
        self.student_name = student_name
        self.student_age = student_age
        self.student_grade = student_grade


# Creating instances of the School class
student1 = School("Alice", 12, "6th Grade")
student2 = School("Bob", 11, "5th Grade")

# Accessing class and instance attributes
print(f"School Name: {School.school_name}, Address: {School.school_address}, Contact: {School.contact_number}")
print(f"{student1.student_name} is in {student1.student_grade}.")
print(f"{student2.student_name} is in {student2.student_grade}.")


"""Inheritance"""


# General class 'Animal'
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} can move")

    def make_sound(self):
        print(f"{self.name} makes a sound")


# Specific class 'Lion' inheriting from 'Animal'
class Lion(Animal):
    def roar(self):
        print(f"{self.name} roars loudly")


# Specific class 'Tiger' inheriting from 'Animal'
class Tiger(Animal):
    def growl(self):
        print(f"{self.name} growls menacingly")


# Creating instances of specific animals
lion = Lion("Simba")
tiger = Tiger("Sher Khan")

# Using inherited methods
lion.move()         # Lion can move
lion.make_sound()   # Lion makes a sound
lion.roar()         # Simba roars loudly

tiger.move()        # Tiger can move
tiger.make_sound()  # Tiger makes a sound
tiger.growl()       # Sher Khan growls menacingly

"""Assuming that your parents don’t have purple hair, you’ve just overridden the hair color attribute that you inherited 
from your parents:"""


class Parent:
    hair_color = "brown"


class Child(Parent):
    hair_color = "purple"   # overridden attribute


p = Parent()
print(p.hair_color)

c = Child()
print(c.hair_color)


"""
Now imagine you decide to learn a second language, like German. In this case, you’ve extended your attributes because 
you’ve added an attribute that your parents don’t have:
"""


class Parent:
    speaks = ["English"]


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")    # extended attributes because you've added an attribute that your parents don't


p = Parent()
print(p.speaks)

c = Child()
print(c.speaks)
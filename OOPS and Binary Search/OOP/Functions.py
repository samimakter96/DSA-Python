"""A class named 'Student' with String variable 'name' and integer variable 'roll_no' and Constructor is already create

Create a method display to print the attributes name and roll_no.

"""


class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(self.name)
        print(self.roll_no)


obj1 = Student("samim", 10)
obj1.display()

obj2 = Student("Rahul", 1)
obj2.display()
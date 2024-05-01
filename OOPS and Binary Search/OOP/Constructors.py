"""Create a class named 'Student' with String variable 'name' and integer variable 'roll_no'.

Create a constructor through which you can assign values through objects on creation of objects.

if No value is passed through object then by default name should be initialized to "john" and roll_no as 2
"""


class Student:

    def __init__(self, name="john", roll_no=2):
        self.name = name
        self.roll_no = roll_no


def main():
    x = Student("Ankit", 101)
    print(x.name)
    print(x.roll_no)

    y = Student("Rahul", 10)
    print(y.name, y.roll_no)

    obj = Student()     # it prints the default value we gave in the constractor
    print(obj.name)
    print(obj.roll_no)


main()

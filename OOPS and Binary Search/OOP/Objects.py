"""Create a class Employee Having 3 attributes (name, year of joining, address)

Create a constructor to initialize the attributes in realtime on object creation.

Create a function print_details to print the details of the employee. (it should be just separated by a space)."""


class Employee:

    def __init__(self, name, year_of_joining, address):
        self.name = name
        self.year_of_joining = year_of_joining
        self.address = address

    def print_details(self):
        print(self.name+" "+str(self.year_of_joining)+"  "+self.address)     # it should be just separated by a space


# Do Not change the Below code Method


def main():
    t = Employee("ram", 1992, "Bangalore")
    t.print_details()

    x = Employee("shyam", 2010, "Lucknow")
    x.print_details()

    y = Employee("babu_rao", 2015, "Delhi")
    y.print_details()


main()


# t, x, y are the objects that are created from the Employee class

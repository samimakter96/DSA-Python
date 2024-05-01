class Member:
    def __init__(self, name, age, phone_no, address, salary):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
        self.salary = salary

    def print_salary(self):
        print(self.salary)


class Employee(Member):
    def __init__(self, name, age, phone_no, address, salary, specialization):
        super().__init__(name, age, phone_no, address, salary)
        self.specialization = specialization

    def print_details(self):
        print(self.name)
        print(self.specialization)
        super().print_salary()


class Manager(Member):
    def __init__(self, name, age, phone_no, address, salary, department):
        super().__init__(name, age, phone_no, address, salary)
        self.department = department

    def print_details(self):
        print(self.name)
        print(self.department)
        super().print_salary()


# Do Not change the Below code Method


def main():
    obj = Employee("Ram", 25, "7003", "Bangalore", 1000, "CSE")
    obj.print_details()

    obj1 = Employee("Shyam", 250, "8098", "Chennai", 2000, "civil")
    obj1.print_details()

    obj_man = Manager("babu", 100, "1234", "Bangalore", 1000, "JP")
    obj_man.print_details()

    obj1_man = Manager("Rao", 250, "456", "Kerala", 3000, "GC")
    obj1_man.print_details()


main()

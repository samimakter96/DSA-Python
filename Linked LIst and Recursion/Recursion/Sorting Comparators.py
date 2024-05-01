"""
we need to sort the name in ascending order and score in descending order.
"""

from functools import cmp_to_key


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{'name': {self.name}, 'score': {self.salary}}"

    @staticmethod
    def comparator(a, b):
        if a.salary > b.salary:
            return -1
        if a.salary < b.salary:
            return 1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0


n = int(input("Enter number of players: "))
data = []

for i in range(n):
    name, salary = input("Enter name and salary: ").split()
    salary = int(salary)
    employee = Employee(name, salary)
    data.append(employee)

data = sorted(data, key=cmp_to_key(Employee.comparator))

for i in data:
    print(i.name, i.salary)

"""
Create a class Employee Having 2 attributes (salary , working_hours).

It will contain the following methods :-

1 - 'getInfo()' which takes the salary, number of hours of work per day of employee as parameter and initializes the
attributes. (Note there is no constructor instead get_info method is used)

2 - 'AddSal()' which adds 10 to salary of the employee if it is less than 500. (note you don't have to print or return
 anything)

3 - 'AddWork()' which adds 5 to salary of employee if the working_hours is more than 6 hours. (note you don't have to
 print or return anything)
"""


class Employee:

    def getInfo(self, salary, working_hours):
        self.salary = salary
        self.working_hours = working_hours

    def AddSal(self):
        if self.salary < 500:
            self.salary += 10

    def AddWork(self):
        if self.working_hours > 6:
            self.salary += 5


# Do Not change the Below code Method

def main():
    t = Employee()
    t.getInfo(400, 7)
    t.AddSal()
    t.AddWork()
    print(t.salary)
    x = Employee()
    x.getInfo(600, 8)
    x.AddSal()
    x.AddWork()
    print(x.salary)


main()
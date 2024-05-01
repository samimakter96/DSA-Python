# Single Inheritance
class A:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    def Add(self):
        print("Addition:", self.num1 + self.num2)

    def Sub(self):
        print("Subtraction", self.num1 - self.num2)


class B(A):
    def Multi(self):
        print("Multiplication", self.num1 * self.num2)

    def Div(self):
        print("Division", self.num1 / self.num2)

    def Rem(self):
        print("Reminder", self.num1 % self.num2)


# obj = A()
# obj.Add()
# obj.Sub()
""" Using Child object we can use Parents properties"""
obj = B()
obj.Add()
obj.Sub()
obj.Multi()
obj.Div()
obj.Rem()

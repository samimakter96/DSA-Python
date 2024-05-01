class Father:
    surname = "Roy"

    def show(self):
        print("My surname is", self.surname)


class Son1(Father):

    def display(self):
        print("My name is Ankit", self.surname)


class Son2(Father):
    def dis(self):
        print("My name is Samir", self.surname)


s1 = Son1()
s2 = Son2()

s1.display()
s1.show()

s2.dis()
s2.show()

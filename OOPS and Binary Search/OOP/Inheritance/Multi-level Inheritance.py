class Father:
    surname = "Singh"


class Son(Father):
    def show(self):
        print("Akash", self.surname)


class GrandSon(Son):
    def display(self):
        print("Ankit", self.surname)


s = Son()
s.show()

Gs = GrandSon()
Gs.display()
Gs.show()
class A:
    _a = 10   # protected
    __b = 20    # private

    def show(self):
        print("a= ", self._a)
        print("b= ", self.__b)


obj = A()
obj.show()

print("Outside of class", A._a)   # we can access protected using through class/obj
# print("Outside of class", A.__b)   # we can't access __b because it's private

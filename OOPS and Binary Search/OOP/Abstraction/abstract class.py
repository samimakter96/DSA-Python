from abc import ABC, abstractmethod


class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")

    @abstractmethod
    def speed(self):
        pass


class Maruti(Car):
    def speed(self):
        print("speed is 100km/h")


class Suzuki(Car):
    def speed(self):
        print("speed is 70km/h")


obj = Maruti()
obj.show()
obj.speed()


obj2 = Suzuki()
obj2.show()
obj2.speed()

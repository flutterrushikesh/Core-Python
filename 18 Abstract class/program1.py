from abc import ABC, abstractmethod
class Hyundai(ABC):
    def slogun(self):
        print("New thinking, new Resposibilities")

    @abstractmethod
    def carType(self):
        print("In sedan")
class Verna(Hyundai):
    def carType(self):
        pass

class Creata(Hyundai):
    def carType(self):
        print("SUV")

obj=Creata()
obj.carType()

import abc as abstractmethod
class Parent:
    def property(self):
        print("Gold, Banglow")
    
    @abstractmethod
    def carrier(self):
        pass
class Child(Parent):
    def carrier(self):
        print("Doctor")
obj=Child()
obj.carrier()
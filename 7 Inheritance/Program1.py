#Inheritance

class company:
    x=10
    def __init__(self, compName,loc):
        print("In constructor")
        self.compName=compName
        self.loc=loc
    
    def compInfo(self):
        print(self.compName)
        print(self.loc)
    
class employee(company):
    pass

obj=company("Microsoft", "Bengluru")
obj2=company("Microsoft", "Pune")
obj.compInfo()
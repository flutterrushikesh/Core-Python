class company:
    
    def __init__(self,compName, loc):
        print("In constructor")
        self.compName=compName
        self.loc=loc

    def compInfo(self):
        print(self.compName)
        print(self.loc)
class employee(company):
    pass

obj1=employee("Microsoft", "Pune")
obj2=employee("Microsoft", "Bengluru")

obj1.compInfo()
obj2.compInfo()
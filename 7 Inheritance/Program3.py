class demo:
    def __init__(self):
        print("In constructor")
        self. x=10
        self.y=20

    def setData(self,z):
        self.z=z

    def printData(self):
        print(self.x)
        print(self.y)
        print(self.z)
obj1=demo()
obj1.setData(30)
obj1.printData()

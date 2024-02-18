class parent:
    def __init__(self):
        print("In parent constructor")
        self.x=10
        self.y=20

    def printData(self):
        print(self.x)
        print(self.y)

class child(parent):
    pass

obj1=child()
obj1.printData()
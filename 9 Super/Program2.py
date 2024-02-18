class parent:
    def __init__(self):
        print("In parent constructor")

    def parentFunc(self):
        print("In parent function")

class child(parent):
    def __init__(self):
        #way 1 to call parent constructor using super method
        #super().__init__()
        #print(id(super()))
        #way 2 to call parent constructor using parent object creation
        parent()
        print(id(parent))
        print("In child constructor")

    def childFunc(self):
        print("In child function")
obj1=child()
obj1.parentFunc()
obj1.childFunc()
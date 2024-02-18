class parent:
    def __init__(self):
        print("In parent constructor")

    def parentFunc(self):
        print("In parent Function")

class child(parent):
    pass

obj1=parent()
obj1.parentFunc()
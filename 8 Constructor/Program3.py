class parent:
    def __init__(self):
        print("In parent constructor")

    def parentFunc(self):
        print("In parent func")
    
class child(parent):
    def __init__(self):
        print("In child constructor")

obj=child()
obj.parentFunc()
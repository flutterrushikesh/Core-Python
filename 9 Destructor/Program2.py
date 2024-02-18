class parent:
    def __init__(self):
        print("In constructor")

    def __del__(self):
        print("In destructor")
    
obj1=parent()
obj2=parent()
obj3=obj1
del obj1

print("End code")
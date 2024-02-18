#parent class
class parent: 
    z=30  #in class nameSpace it is accessible in instance or class method
    def __init__(self): #constructor of parent class it is calls when object create
        print("In parent constructor")
        self.x=10
        self.y=20
    
    def dispData(self): #instance method it access the instance or class variable
        print(self.x)
        print(self.y)

    @classmethod #class method it is access only class variables
    def DisParent(cls):
        print(cls.z)

    #destructor destroy the object when execucation is exit.
    #it call automatically when object will be destroyed
    #destructor is same as del obj1
    def __del__(self): 
        print("In destructor")

obj1=parent()
obj1.dispData()
obj1.DisParent()
del obj1
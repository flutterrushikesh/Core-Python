class Demo:
    def __init__(self):
        self.x=10 #public variable
        self._y=20 #protected variable
        self.__z=30 #private variable

    def __fun(self): #private variable
        print("In fun function")
    
print(dir(Demo)) #Print all methods present in class
obj1=Demo() #object creation
print(dir(obj1)) #Print all methods present in object
print(obj1.x) #normally print
print(obj1._y)   # protected normaly printed
print(obj1._Demo__z) #Access using class name (i.e name mangling)
obj1._Demo__fun() #calling using class name but fun() is instance method but internally call by class name 
#because fun() method is private

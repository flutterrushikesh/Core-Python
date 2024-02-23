class demo:
    z=30  #public
    def __init__(self):
        self._x=10 #protected
        self.__y=20 #private
print(dir(demo)) #Internally  dir call this(__dir__) method 
obj1=demo()
print(dir(obj1))
print(obj1._x)
print(obj1.z)
print(obj1._demo__y) #no error because it accessible using name Mangling(by class name)
 #it access the __y instance variable using name Mangling(__y it change the by class name.)
#_className__variable_name for prof check in class   print(dir(className))
#in object print(dir(objectName))

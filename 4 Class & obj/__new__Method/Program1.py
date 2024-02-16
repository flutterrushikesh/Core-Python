class Employee:
    def __new__(cls):
        print("Create")
        return object.__new__(cls)
        
    def __init__(self):
        print("In constructor")
Employee()
 #new method responsible for creatig a new instace of the class
#it takes the (cls) as its first argument asnd return a nre intance of class
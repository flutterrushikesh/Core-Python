class parent1: #Parent1

    def __init__(self): #parent1 constructor
        print("in parent constructor: 1")

    def dispData(self): #instance method of class parent1
        print("In dispData")

class parent2: #class parent 2
    def __init__(self): #parent2 constructor
        print("in parent constructor: 2")

    def printData(self): #parent2 instance method
        print("In prindata")

class child(parent2, parent1): 
    pass 

obj1=child() #object reation

# it calls the the parent2 constructor because it has left hand side pariority ie (parent2, parent1)
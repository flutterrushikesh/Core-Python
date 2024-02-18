class  parent1: #parent class1

    def dispData(self):
        print("In dispData")

class parent2: #parent class 2

    def printData(self): 
        print("In printdata")

class child(parent1, parent2): #child class inherit to parent1 and parent 2
    pass 

obj1=child() #object creation
obj1.dispData() #calling method
obj1.printData() #calling method

#all inherited to child class 
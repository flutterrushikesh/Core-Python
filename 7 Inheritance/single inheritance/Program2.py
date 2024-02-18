#Inheritance 
#all methods/ properties/ variable are inherited to child class
class parent: #parent class
    def __init__(self): #constructor
        print("In parent constructor")
    
    def carrier(self): #instance method
        print("Engg")

    def marry(self): #instance method
        print("Dipika padukun")

class Child(parent):#parent class inherit to child class
    def __init__(self): # child constructor
        print("In child constructor") 
    
    def carrier(self): #child instance method
        print("Doc/adv")

    def marry(self): #child instance method
        print("Your choice")

obj1=Child() # creater child class object
obj1.carrier() #calling carrier method 
obj1.marry() #calling marry method


'''in that senario all method or constructor call child.
because all inherited to parent class'''
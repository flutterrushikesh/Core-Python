class parent: #parent class
    def __init__(self): #initilize constructor & instance vaiable
        print("In parent constructor")

    def carrier(self): #parent method & instance method
        print("Youtuber")
    
    def marry(self): # parent method & instance method
        print("Dipika padukun")
class child(parent): #extends parent class 
    pass  #It has no body

obj1=child() #object creation
obj1.carrier() #it calls parent method
obj1.marry() #it calls parent method
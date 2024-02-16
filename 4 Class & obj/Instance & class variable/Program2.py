class Employee:
    compName="Facebook" #class variable
    #constructor
    def __init__(self):
        print("In constructor")
        self.empid=12   #instance variable
        self.empName="Kanha"    #instance variable

    #instance method
    def empInfo(self):
        print(self.empid)
        print(self.empName)
        print(self.compName) #class variable access in instance method
#object creation
emp1=Employee()
emp2=Employee()
emp1.empInfo() 
emp2.empInfo()


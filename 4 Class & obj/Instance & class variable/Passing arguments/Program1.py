#Passing arguments from object to constructor
class Employee:
    compName="Facebook"

    def __init__(self , empid, empName):
        print("In constructor")
        self.empid=empid
        self.empName=empName

    def empInfo(self):
        print(self.empid)
        print(self.empName)

emp1=Employee(12, "Kanha")
emp2=Employee(15, "Ashish")
emp1.empInfo()
emp2.empInfo()
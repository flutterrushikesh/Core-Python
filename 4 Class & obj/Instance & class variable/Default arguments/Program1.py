class Employee:
    def __init__(self, empid=0, empName=None):
        print("In constructor")
        self.empid=empid
        self.empName=empName
    def empInfo(self):
        print(self.empid)
        print(self.empName)
emp1=Employee(12, "Kanha")
emp2=Employee(15, "Ashish")
emp3=Employee()
emp1.empInfo()
emp2.empInfo()
emp3.empInfo()
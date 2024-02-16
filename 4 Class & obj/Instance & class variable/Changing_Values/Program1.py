class Employee:
    def __init__(self):
        print("In constructor")
        self.empid=12
        self.empName="Kanha"

    def empInfo(self):
        print(self.empid)
        print(self.empName)

emp1=Employee()
emp2=Employee()
emp1.empInfo()
emp2.empInfo()
emp1.empid=50
emp1.empName="Badhe"
emp1.empInfo()
emp2.empInfo()
class Company:
    compName="Facebook" #In class namespace
    
    def __init__(self):
        print("In constructor")
        self.empid=12
        self.empName="Kanha"

    def compInfo(self):
        print(self.empid)
        print(self.empName)
        print(Company.compName)  #In class Namespace

emp1=Company()
emp1.compInfo()
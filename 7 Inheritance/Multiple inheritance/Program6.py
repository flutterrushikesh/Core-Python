class Boss:
    def report(self):
        print("In reporter: Boss")
class Manager1(Boss):
    def report(self):
        print("In report: Manager1")
class Manager2(Boss):
    def report(self):
        print("In report: Manager2")
class Manager3(Boss):
    def report(self):
        print("In report: Manager3")
class Teamlead1(Manager1, Manager3):
    def report(self):
        print("In report: Teamlead1")
class Teamlead2(Manager2, Manager3):
    def report(self):
        print("In report: Teamlead2")
class Developer(Teamlead1, Teamlead2):
    def report(self):
        print("In report: Developer")
obj1=Developer()
obj1.report()
print(Developer.mro())
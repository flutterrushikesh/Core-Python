class Boss:
    def report(self):
        print("In report:Boss")
class Manager1(Boss):
    pass
class Manager2(Boss):
    def report(self):
        print("In report: Manager2")
class Manager3(Boss):
    pass
class Teamlead1(Manager1, Manager3):
    pass
class Teamlead2(Manager2, Manager3):
    def report(self):
        print("In report: Teamlead2")
class Developer(Teamlead1, Teamlead2):
    pass
obj1=Developer()
obj1.report()
print(Developer.mro())
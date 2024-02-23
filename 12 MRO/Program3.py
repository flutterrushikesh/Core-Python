class Boss:
    def report(self):
        print("Mich Boss Ahe")

class Manager1(Boss):
    def report(self):
        print("Report to Boss")

class Manager2(Boss):
    def report(self):
        print("Report to Boss")

class Teamlead1 (Manager2, Manager1):
    def report(self):
        print("Report to Manager1 & Manager2")
    
class Teamlead2(Manager2, Manager1):
    def report(self):
        print("Report to Manger1 & Manager2")

class Developer(Teamlead1, Teamlead2):
    def report(self):
     print("Report to Teamlead1 & Teamlead2")
obj=Developer()
print(Developer.mro())
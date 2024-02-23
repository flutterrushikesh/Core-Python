class Boss:
    def report(self):
        print("Mich Boss aahe")

class Manager1(Boss):
    def report(self):
        print("Repoer to Boss")
    
class Manager2(Boss):
    def report(self):
        print("Report to Boss")

class Teamlead1(Manager1, Manager2):
    def report(self):
        print("Report to Manager1 & Manager2")
class Teamlead2(Manager2):
    def report(self):
        print("Report to Manager2")
class Developer(Teamlead2, Teamlead1):
    def report(self):
        print("Report to Teamlead1 & Teamlead2")
obj=Developer()
print(Developer.mro())
class Boss:
    def report(self):
        print("Mich Boss Ahe")

class Manager1(Boss):
    def report(self):
        print("Report to Boss")

class Manager2(Boss):
    def report(self):
        print("Report to Boss")
class Manager3(Boss):
    def report(self):
        print("Report to Boss")
class Teamlead1(Manager1, Manager2):
    def report(self):
        print("report to Manager1 & Manager2")
class Teamlead2(Manager2, Manager3):
    def report(self):
        print("Report to Manager2 & Manager3")
class Developer(Teamlead1, Teamlead2):
    def report(self):
        print("Report to Teamlead1 & Teamlead2")
obj=Developer()
print(Developer.mro())
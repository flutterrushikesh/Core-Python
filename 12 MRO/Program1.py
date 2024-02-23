class Boss :
    def report(self):
        print("Mich aahe Boss")
class Manager(Boss):
    def report(self):
        print("Report to boss")
class Teamlead(Manager, Boss):
    def report(self):
        print("Report to boss & Manager")
class Developer(Teamlead):
    def report(self):
        print("Report to Teamlead")
obj=Developer()
print(Developer.mro())
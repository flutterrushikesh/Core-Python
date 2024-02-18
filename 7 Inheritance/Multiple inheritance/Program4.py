class Manager:
    def project(self):
        print("In project: Manager")

class Teamlead1(Manager):
    pass
    
class Teamlead2(Manager):
    def project(self):
        print("In project: Teamlead2")
class Developer(Teamlead1, Teamlead2):
    pass
obj=Developer()
obj.project()
print(Developer.__mro__)
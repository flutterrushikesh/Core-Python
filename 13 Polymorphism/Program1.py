#passing object to function.

class Demo:
    def fun(self):
        print("In fun Demo")
class Memo:
    def fun(self):
        print("In fun Memo")
def callObj(obj):
    obj.fun()
obj1=Demo()
obj2=Memo()

callObj(obj2)
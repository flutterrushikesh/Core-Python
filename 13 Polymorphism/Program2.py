class Demo:
    def fun(self):
        print("In Fun Demo")
class Memo:
    def gun(self):
        print("In Gun Memo")

def callObj(obj):
    '''if obj==obj1:
        obj.fun()
    else:
        obj.gun()'''
    if id(obj)==id(obj1):
        obj.fun()
    else:
        obj.gun()
obj1=Demo()
obj2=Memo()
callObj(obj1)
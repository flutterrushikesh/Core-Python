class Demo:
    def fun(self):
        print("In fun")
class Memo:
    def gun(self):
        print("In Gun")

def callFun(obj):
    if hasattr(obj,'fun'):
        obj.fun()
    elif hasattr(obj,'gun'):
        obj.gun()

obj1=Demo()
obj2=Memo()
callFun(obj2)
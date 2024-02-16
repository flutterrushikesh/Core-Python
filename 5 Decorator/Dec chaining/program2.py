#decor chaining

def decorFun(func):
    print("In decorFunc")

    def wrapper():
        print("in a wrapper 1")
        func()
        print("End wrapper 1")
    return wrapper
def decorRun(func):
    print("In a decorRun")

    def wrapper():
        print("In a wrapper 2")
        func()
        print("End wrapper 2")
    return wrapper
@decorFun
@decorRun
def normalFun():
    print("In a normal fun")

normalFun()

    
class parent:
    def __init__(self):
        print("in constructor")

    def __del__(self):
        print("In destructor")

def fun():
    print("In Function")
    obj1=parent()
    print("End function")

fun()
print("End code")
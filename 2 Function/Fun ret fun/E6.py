def outer():
    def inner1(x,y):
        print("In inner 1")
    return inner1
    print("outer")
retobj=outer()
retobj(10,20)
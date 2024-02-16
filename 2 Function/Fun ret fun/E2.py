def outer(x,y):
    def inner1():
        print("In inner 1")
    print("In outer")
    return inner1
retobj=outer(10,20)

retobj()
def outer(x,y):
    def inner1(a,b):
        print("In inner 1")
        return a+b
    print("In outer")
    print(x+y)
    return inner1
retobj=outer(5,8)
inneret=retobj(3,4)
print(retobj)
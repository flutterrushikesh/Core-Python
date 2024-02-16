def outer():
    def inner1(x,y):
        print("In inner1")
        return x+y
    def inner2(a,b):
        print("In inner 2")
        return a*b
    return inner1, inner2
inn, inn2=outer()
ret1=inn(10,20)
ret2=inn2(3,4)
print(ret1+ret2)
print(inn)
print(inn2)


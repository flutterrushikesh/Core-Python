def outer():
    def inner1():
        print("In inner1")
    def inner2():
        print("In inner2")
    return inner1, inner2
'''inn1, inn2=outer()
inn1()
inn2()
'''
retobj=outer()
for i in retobj:
    i()
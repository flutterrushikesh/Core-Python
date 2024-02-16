def outfun():

    def inner1():
        print("In inner 1")
    def inner2():
        print("In inner 2")
    print("in outer ")
    inner1()
    inner2()
outfun()

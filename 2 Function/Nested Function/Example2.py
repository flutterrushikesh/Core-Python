def outfun() :
    def inner1():
        print("in inner")
    print("in outer")
outfun().inner1()
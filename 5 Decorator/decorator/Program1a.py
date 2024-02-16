def decorFun(func):
    print("In DecorFun")

    def Wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")
    return Wrapper
def normalFun():
    print("Hellow in normal Fun")

normalFun=decorFun(normalFun)
normalFun()
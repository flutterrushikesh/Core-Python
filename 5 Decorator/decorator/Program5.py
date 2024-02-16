
def decorFun(func):
    print("In a decor fun")

    def wrapper(*args):
        print("In a wrapper")
        val=func(*args) 
        print("End wrapper")
        return val
    return wrapper
@decorFun
def normalFun(x,y):
    print("In a normal function")
    return x+y
#normalFun=decorFun(normalFun)
print(normalFun(10,20)) 

'''Explanation
1.call the notmalFun but above normalfun @decorfun mentioned and he will passed normalfun as a
parameter and returns the address of wrapper function

2.normalfun calls the wrapper function
3.the *args store many value i.e argunment passed
4.val is used for store value from *args
5.returns val from that function
6.call the normalfun and he will returns the addition of x+y
'''


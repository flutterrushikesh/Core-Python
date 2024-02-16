#outer function
def run(): 
    print("In Run") 

#outer function
#passing function as  argument to fun(x)
#and call to this argument
def fun(x):
    print("In fun")
    x()

#passed function as argument
fun(run)
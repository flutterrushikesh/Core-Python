#actual Decorator

#outer function
def decorFun(func): #From @decorfun() calls here
    print("In decorFun")

    #inner Function
    def wrapper():  
        print("Start wrapper")
        func() #it calls the parameter of decorfun then return here and flow of code continiue
        print("End wrapper")
    return wrapper

#for normalFun call then he will see @decorfun()
#actual decorator usesed here
@decorFun #It calls the decorfun function
def normalFun(): #outer fun
    print("hellow in nomal Fun")

#normalFun=decorFun(normalFun) #by default @decorFun line exwcutes
  #it calls the normalFun but above he see @decorfun class
            #there.

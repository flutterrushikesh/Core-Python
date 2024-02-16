def outerFun(): #outer function 
    print("In outer Fun")

    def innerFun1(): #inner function
        print("In inner Fun1")

    def innerFun2(): #inner Function
        print("In inner Fun2")

    innerFun1() # calling inner Function
    innerFun2() #Calling inner Function
outerFun() # calling outerFUn
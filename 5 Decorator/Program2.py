def outFun1(): #outer function
    print("In outer Function")

    def innerFun1():#inner Function
        print("In Inner Function")

    def innerFun2(): #inner Function
        print("In inner Function2")

    #returns the address of inner functions
    return innerFun1, innerFun2
'''retFun1, retFun2=outFun1()
retFun1() #calling by address
retFun2() #callinf by adress'''

retval=outFun1()# Stores both address in retval
for i in retval: #seperates the both address the for iterator is 2 time
    i()          
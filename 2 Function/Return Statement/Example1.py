def Fact(a):
    prod=1
    for i in range(1, a+1):
        prod=prod*i
    return prod

val=int(input("Enter Val"))

factorial=Fact(val)
print(factorial)
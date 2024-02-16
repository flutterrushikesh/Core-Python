def div(a):
    if(a%4==0 and a%5!=1):
        print(a,"divisible by 4 and 5")
    else:
        print(a,"Not divisible by 4 and 5")
 
num=int(input("Enter number:"))

div(num)
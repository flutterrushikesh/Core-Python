x= int(input("enter value for x:"))
y=int(input("enter value for y:"))
for i in range(x, y+1):
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")
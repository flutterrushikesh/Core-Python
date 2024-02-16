x= int(input("Enter value for x:"))
y=int(input("Enter value for y:"))
for i in range(x, y+1):
    if(i%4==0 and i%5!=0):
        print(i)
    else:
        print(i,"it is not allowed")    
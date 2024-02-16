x=int(input("Enter value"))
for i in range(1, x+1):
    if(i%2==1):
        print(i, end="")
    else:
        print("*", end="")
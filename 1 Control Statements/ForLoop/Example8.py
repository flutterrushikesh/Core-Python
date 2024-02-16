x=int(input("Enter number"))
for i in range(x):
    if(i%3==0):
        print("Three")
    elif(i%5==0):
        print("Five")
    else:
        print(i)
print("out of for")
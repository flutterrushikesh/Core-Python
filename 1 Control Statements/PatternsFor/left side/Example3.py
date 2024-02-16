num=65
for i in range(3):
    for j in range(i+1):
        print(chr(num), end="")
        num+=1
    print()
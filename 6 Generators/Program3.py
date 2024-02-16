def fun(y):
    print("Start fun")
    while y>0:
        yield y
        y+=1
    print("End fun")
ret=fun(20)
print(next(ret))
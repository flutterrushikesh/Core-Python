def fun():
    print("Start Func")
    yield 10
    yield 20
    yield 30
    print("End func")

ret=fun()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
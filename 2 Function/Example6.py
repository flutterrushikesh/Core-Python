def multiply(*argc):
    result=1
    for i in argc:
        result=result*i
    return result
result=multiply(2,3,4)
print(result)
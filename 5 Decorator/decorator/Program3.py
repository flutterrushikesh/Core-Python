def sumData(*args): #*args single value stores as passed from funtion
    sumdata=0
    for i in args:
        sumdata=sumdata+i
    return sumdata #returns 30 
print(sumData())

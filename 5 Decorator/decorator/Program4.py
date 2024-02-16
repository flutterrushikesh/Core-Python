def sumData(**args): #**args stores multiple value as argument passed form funtion 
    sumdata=0
    for k,v in args.items():
        sumdata=sumdata+v
    return sumdata
print(sumData(x=10,y=20)) #by default value stores in **args 


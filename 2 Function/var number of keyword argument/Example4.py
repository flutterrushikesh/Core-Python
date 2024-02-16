def fun(**argc):
    for key, value in argc.items():
        print(key,":",value)
        
fun(x=10,z=60, y=20)

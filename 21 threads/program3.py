



import threading 

print("Start code")

def fun():
    print("In fun method")
    print(threading.current_thread().name)
fun()


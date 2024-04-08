

import threading

def fun():
    print("In fun method")
    print(threading.current_thread().name)
    for i in range(1,3):
        print("In Fun")


def mun():
    print("In mun method")
    print(threading.current_thread().name)
    for i in range(1,3):
        print("In Mun")

print(threading.current_thread().name)

thread1=threading.Thread(target=fun)
thread2=threading.Thread(target=mun)

thread1.start()
thread2.start()

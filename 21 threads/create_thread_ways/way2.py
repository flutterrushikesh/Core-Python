

#thread using class and obj


import threading 
from threading import Thread

class Mythread(Thread):
    def run(self):
        print("In run method")
        print("Thread.getName()")

print(threading.current_thread().name)

t1=Mythread()
t1.start()


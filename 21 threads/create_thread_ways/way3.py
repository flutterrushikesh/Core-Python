

#Using func parameter

import threading 
from threading import Thread

class MyThread(Thread):
    def __init__(self, x,y):
        threading.thread.__init__(self)
        self.x
        self.y

    def run(self):
        print("In run method")
        print(self.x)
        print(self.y)
        print(threading.current_thread().getName())

print(threading.current_thread().getName())
t1=MyThread(10,20)
t1.start()

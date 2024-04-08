




import threading, os

for i in range(1,10):
    print(i)

print(os.getpid())#PVM Process Id
print(threading.current_thread().name)

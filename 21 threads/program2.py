



import threading

print("One")
print("Two")
print("Three")

print(threading.current_thread().name)


#In that senario the flow of output will normal because you can not use of threading.
#you prints only name of thread

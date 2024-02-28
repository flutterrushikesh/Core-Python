fileObj=open("incubator.txt", "r")

try:
    #fileObj.read()
    fileObj.write("Welcome to Incubator")
except:
    print("File Not found")
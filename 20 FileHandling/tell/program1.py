


#tell()
#It shows the currunt position of cursor


fileObj=open("row.txt", "r")
print(fileObj.tell())
print(fileObj.read(), end="")
print(fileObj.tell(), end="")

#There are 2 types of file
#1. Text file eg: .txt
#2. BInary file eg: .jpeg, .png

#Opening $ closing file.

#In python byDefault Sets a readMode 
#to read any file please check the this file is present or not.


fileObj=open("Core2Web.txt")
fileObj.write("Hellow Core2Web")

# Error because this file is not writable, python sets bydefault file readMode.


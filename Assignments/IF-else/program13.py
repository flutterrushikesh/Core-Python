#Write a program to print the month name according to the month number.
#Input : 1
#Output: January

#Input: 2
#Output: February
#Input: 13
#Output: Invalid input for month


month=int(input("Enter a month number"))
if(month==1):
    print("January")
elif(month==2):
    print("February")
elif(month==3):
    print("March")
elif(month==4):
    print("April")
elif(month==5):
    print("May")
elif(month==6):
    print("June")
elif(month==7):
    print("July")
elif(month==8):
    print("August")
elif(month==9):
    print("September")
elif(month==10):
    print("October")
elif(month==11):
    print("November")
elif(month==12):
    print("December")
else:
    print("Enter a valid month number!!!")

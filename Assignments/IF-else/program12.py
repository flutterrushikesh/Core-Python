#Write a program to check the day number(1-7) and print the corresponding day of week.
#Input : 1
#Output: Monday
#Input : 7
#Output: Sunday
#Input : 8
#Output: day number must be between 1 to 7!!!!

weekdays=int(input("Enter day number:"))
if(weekdays==1):
    print("Monday")
elif(weekdays==2):
    print("Tuesday")
elif(weekdays==3):
    print("Wednesday")
elif(weekdays==4):
    print("Thursday")
elif(weekdays==5):
    print("Friday")
elif(weekdays==6):
    print("Saturday")
elif(weekdays==7):
    print("Sunday")
else:
    print("Day number must be between 1 to 7!!!")

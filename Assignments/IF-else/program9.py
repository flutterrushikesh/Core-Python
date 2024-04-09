#Write a program to check whether the given number is divisible by 3 or 7.
#Input: 15
#Output: 15 is divisible by 3
#Input: 28
#Output: 28 is divisible by 7
#Input: 20
#Output: 20 is neither divisible by 3 nor by 7.

input1=int(input("Enter value: "))
if(input1%3==0):
    print(input1, "is divisible by 3")
elif(input1%7==0):
    print(input1, "is divisible by 7")
else:
    print(input1, "is neither divisible by 3 or by 7")

#iWrite a program to check if the given number is divisible by 2,5,10 or not, if not then print a message “Is Not Divisible By 2,5,10”.(take hardcoded values)
#Input: num = 10
#Output: 10 is divisible by 2,5,10
#Input: num = 15
#Output: 15 Is Not Divisible By 2,5,10

num1=10
if(num1%2==0 and num1%5==0 and num1%10==0):
    print(num1, "is divisible by 2, 5, 10")

num2=15
if(num2%2!=0 or num2%5!=0 or num2%10==1):
    print(num2, "is not divisible by 2,5,10")

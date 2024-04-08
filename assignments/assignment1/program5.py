#Write a program to check whether the given number is even or odd and also check
#whether the given number is greater than 10 or not. (take hardcoded values)
#Input: num =13;
#Output: 13 is an odd number and greater than 10.
#Input: num =8;
#Output: 8 is an even number and less than 10;
#Input: num =10;
#Output: 10 is an even number and equal to 10;

num1=13
num2=8
num3=10
if(num1%2!=0 and num1>=10):
    print(num1, "is an odd number and greater than 10")


if(num2%2==0 and num2<=10):
    print(num2, "is an even and less than 10")


if(num3%2==0 and num3<=10):
    print(num3, "is an even and equal to 10")


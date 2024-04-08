#Write a program to check the even or odd numbers from given list.

numList=[10,28,89,27,56,78,99]
for num in numList:
    if(num%2==0):
        print(num, "is even number")
    else:
        print(num, "is odd number")

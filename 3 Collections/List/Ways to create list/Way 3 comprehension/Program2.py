Normal_list=[num for num in range(1,11)]
print(Normal_list)


#first excute for loop and ji kahi value yeil ti num madhe save hoii
even_list=[num*num for num in range (1,11)if num%2==0]
print(even_list)


#first excute for loop and ji kahi value yeil ti num madhe save hoii
odd_list=[num*num for num in range (1,11)if num%2==1]
print(odd_list)

#internal code of even_list=[num*num for num in range (1,11)if num%2==0] of this line
'''
even_list=list()
for num in range(1,11):
    if num%2==0:
        even_list.append(num)
        print(num)
'''
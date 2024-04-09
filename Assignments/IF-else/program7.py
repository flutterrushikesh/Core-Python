#Write a program to check the character upercase or lower case from the following list.


chrList=['a', 'B', 'Z', 'F', 'u','i','P','W','J']
for singleChr in chrList:
    if(singleChr>=chr(97)):
        print(singleChr, "is a lowercase character")
    else:
        print(singleChr, "is a upercase character")

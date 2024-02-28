#Append

f1=open("Core.txt","a")

friends=["Sangam\n", "Rohan\n", "Sumit\n", "Shardul\n"]

for friend in friends:
    f1.write(friend)
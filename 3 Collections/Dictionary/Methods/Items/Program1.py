#items() - it used for for loop only

player={18:"Rohit", 77:"Shubman", 18:"Virat", 1:"KL Rahul", 96:"Shreyas",63:"SKY",8:"Jaddu"}
print(player)

player.items()
for key,value in player.items():
    print(key,":",value)
playerList=["rohit", "shubman", "virat", "iyer","Rahul"]
PlayerName=input("Enter a player Name:")
count=0
for player in playerList:
    count=count+1
    if(player==PlayerName):
        print(PlayerName, "in a list")
        break
print("count is", count)

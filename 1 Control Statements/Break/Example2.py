playerList=["rohit", "shubman", "virat", "iyer","Rahul"]
PlayerName=input("Enter a player Name:")

for player in playerList:

    if(player==PlayerName):
        print(PlayerName, "in a list")
        break
    else:
        print(PlayerName, "not in list")



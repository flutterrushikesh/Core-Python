#call from @college and as a argument room passed
def college(parent):
    print("In a college")

       
    def movie():
        print("In a movie")
        parent() # he call the argument of college 
        print("End movie")
    return movie #returns the address of movie function to room() at the time of call
@college # by default this line executed room=college(room)
def room():
    print("In a room")

room() #he stores the address of movie funtion


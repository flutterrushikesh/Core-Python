def Education(func):
    def college():
        print("In a college")
        func()
        print("End college")
    return college

def timePass(func):
    def movie():
        print("In a movie")
        func()
        print("End movie")
    return movie

def classes(func):
    def core2web():
        print("In a core2web")
        func()
        print("End core2web")
    return core2web

@Education
@timePass
@classes
def room():
    print("In a room")
room()
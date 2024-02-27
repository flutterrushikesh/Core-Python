
class ICC:
    def __init__(self):

        print("In ICC Constructor")
class BCCI(ICC):
    def __init__(self):
        print("In BCCI constructor")

class IPL(BCCI):
    def __init__(self):
        print("In IPL constructor")

obj=ICC()


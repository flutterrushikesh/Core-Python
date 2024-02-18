class A:
    def fun(self):
        print("In Fun : A")

class B:
    def fun(self):
        print("In Fun : B")

class C:
    def fun(self):
        print("In fun : C")

class D(A,B):
    def fun(self):
        print("In Fun : D")
        super().fun()

class E(B,C):
    def fun(self):
        print("In fun : E")
        super().fun()

class F(D,E):
    def fun(self):
        print("In fun : F")
        super().fun()

obj1=F()
obj1.fun()
print(F.__mro__) # it shows the how code works

#MRO= Method resoulution order
#DFA= Deapth first algorithm
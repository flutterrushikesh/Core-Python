#Set
'''
1.set is a internally dict.
2.set does not have an index.
3.set does'nt allow duplicate data.
4.set used intenally hashcode.
'''
setdata1=set()
print(setdata1)

setdata2={1,2,3,4,5}
print(setdata2)

setdata3={1,"A",10.5,0,True,False}
print(setdata3)

setdata4={"Ashish", "Kanha", "Bade", "Rahul"}
print(setdata4)

setdata5=set([10,20,30,40,50]) #passing argument to set constructor
print(setdata5)

#setdata6=set(10,20,30,40,50)
#print(setdata6)
#error beacause set constructor have required 1 arugument and 5 is given

setdata7=set("shashi")
print(setdata7)

#setdata8=set(10)
#print(setdata8)
#eeror bevause int type is not itteral
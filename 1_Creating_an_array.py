import numpy as np
a=np.array([1,2,3,4,5,6])
print(a) 
print(type(a)) #type of array

lst=[]
for i in range(1,5):
    j=int(input(""))
    lst.append(j)
print(np.array(lst))
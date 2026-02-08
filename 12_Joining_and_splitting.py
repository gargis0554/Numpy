import numpy as np

var=np.array([1,2,3,4])
var1=np.array([9,8,4,5])

a=np.concatenate((var,var1))
print(a)
print()

#2d
var3=[[1,2],[3,4]]
var4=[[3,4],[5,6]]
arr=np.concatenate((var3,var4),axis=1)
print()
b=np.stack((var3,var4),axis=1)
print(b)
print()
c=np.hstack((var3,var4))
print(c)
print()
d=np.vstack((var3,var4))
print(d)
print()
e=np.dstack((var3,var4))
print(e)

#splitting
arr=np.array_split(var3,3,axis=1)
print(arr)
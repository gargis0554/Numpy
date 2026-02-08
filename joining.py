import numpy as np

s=np.array([1,2,3])
t=np.array([4,5,6])
print(np.concatenate((s,t)))

# 2D with rows(axis=1)

g=np.array([[1,2],[4,3]])
h=np.array([[7,8],[5,6]])
print(np.concatenate((g,h),axis=1))

# stack funtion
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.stack((a,b),axis=1))

# hstack()
c=np.array([1,2,3])
d=np.array([4,5,6])
print(np.hstack((c,d)))

# vstack
c=np.array([1,2,3])
d=np.array([4,5,6])
print(np.vstack((c,d)))

# dstack
c=np.array([1,2,3])
d=np.array([4,5,6])
print(np.dstack((c,d)))
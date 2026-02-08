import numpy as np

print(np.__version__)

x=np.array([1,2,3,4])
print(x)
print(type(x))
y=np.array((1,2,3,4))
print(y)
print(type(y))

# 0d array
z=np.array(42)
print(z)
# 1d array
d=np.array([3,4,6,7])
# 2d array
t=np.array([[1,2,3],[4,5,6]])
print(t)
# 3d array with two 2d array
three=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[4,6,8]]])
print(three)
# check dimension
print(three.ndim)
print(t.ndim)
print(d.ndim)
# create a array with 5d and verify its 5 dimension
f=np.array([1,2,3,4,5], ndmin=5)
print(f)
# array indexing
print(d[1])
print(t[0,-1])
print(three[-1,0,2])

# array slicing
print(d[2:-1])
g=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(g[1,1:4])
print(g[0:2,2])
print(g[0:2,1:4])

# data types in numpy
k=np.array([1,2,3,4])
ban=np.array(['apple','banana','cherry'])
print(k.dtype)
print(ban.dtype)

# creating array with a defined data type
k=np.array([1,2,3,4],dtype='S')
print(k)
print(k.dtype)

# creating a array with 4 byte integer
sharad=np.array([1,2,3,4],dtype='i4')
print(sharad)
print(sharad.dtype)

# converting data type in existing array-astype()
sharad=np.array([1.1,1.2,3.3])
shar1=sharad.astype('i')
print(shar1)
print(shar1.dtype)
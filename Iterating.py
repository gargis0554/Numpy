import numpy as np

g=np.array([1,2,3])
for i in g:
    print(i)
# 2D
t=np.array([[1,2,3],[4,5,6]])
for i in t:
    print(i)

s=np.array([[1,2,3],[4,5,6]])
for i in s:
    for j in i:
        print(j)

# 3D
s=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in s:
    for j in i:
        for k in j:
            print(k)
# nditer()
s=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in np.nditer(s):
    print(i)

t=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(t[:,::2]):
    print(i)


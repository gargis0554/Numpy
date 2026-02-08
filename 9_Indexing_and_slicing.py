import numpy as np

d=np.array([1,2,3,4,5,6,7,8,9])
print(d[1:5]) #(start:stop:step)

t=np.array([[1,2,3],[2,3,4]])
print(t[1,1:]) 

y=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(y[1,1,0:])
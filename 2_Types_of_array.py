#there are different types of array: 1D 2D 3D etc.
#1D
import numpy as np

x=np.array([1,2,3,4])
print(x.ndim)#1d

y=np.array([[1,2],[3,4],[5,6]])
print(y.ndim)#2d

z=np.array([[[1,2],[3,4]],[[5,6],[6,7]]])
print(z.ndim)#3d


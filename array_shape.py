import numpy as np

d=np.array([1,2,3,4],ndmin=5)
t=np.array([[2,3,6,7],[4,5,6,7]])
print(d)
print(d.shape)
print(t.shape)

# reshaping
import numpy as np
sharad=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
sharad1=sharad.reshape(4,3)
sharad2=sharad.reshape(2,3,2)
print(sharad1)
print(sharad2)

# view or copy
shar=np.array([1,2,3,4,5,6,7,8])
print(shar.reshape(2,4).base)    

# unknown dimension 
import numpy as np
sharad=np.array([1,2,3,4,5,6,7,8])
sharad1=sharad.reshape(2,2,-1)
print(sharad1)

# flattening the array by converting multidimensional array in 1-D
import numpy as np
sharad=np.array([[1,2,3],[4,5,6]])
sharad1=sharad.reshape(-1)
print(sharad1)

'''there are alots of function for changing the shape of an array in numpy. like flatten,ravel and also
rearanging the element rot90,flip,flipir,flipud. they all are 
actually comes under advanced numpy.
'''
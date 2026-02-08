import numpy as np
var=np.matrix([[1,2],[3,4]])
print(var.dot(var.T))
print()
#tranpose
print(np.transpose(var))
print()
#swapaxes
print(np.swapaxes(var,0,1))
print()
#inverse
print(np.linalg.inv(var))
print()
#matrix_power
print(np.linalg.matrix_power(var,2))
#determinate
print(np.linalg.det(var))
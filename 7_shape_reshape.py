import numpy as np

var=np.array([[1,2],[1,2]])
print(var.shape) #(2, 2)

f=np.array([[[[1,2,34]]]])
print(f.shape) #(1, 1, 1, 3)

var2=np.array([1,2,3,4,5,6])
x=var2.reshape(3,2)
#[[1 2]      
# [3 4]      
# [5 6]]
print(x)

print(x.reshape(-1)) #1d me fir reshape ho gya

import numpy as np

#array filled with 0s
zero=np.zeros(10)
print(zero) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#2d zero
i=np.zeros((3,4))
print(i)
#[[0. 0. 0. 0.]
#[0. 0. 0. 0.]
#[0. 0. 0. 0.]]

#array filled with ones
one=np.ones(10)
print(one) #[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

#empty array
e=np.empty(4)
print(e) #[8.57050243e-312 8.57050243e-312 0.00000000e+000 0.00000000e+000]

#an array with range of element
a=np.arange(6)
print(a) #[0 1 2 3 4 5]

#array diagonal element with 1's
y=np.eye(3)
print(y)
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]

#linspace function : it divides the array into parts
z=np.linspace(1,10,num=5)
print(z)
#[ 1.    3.25  5.5   7.75 10.  ]
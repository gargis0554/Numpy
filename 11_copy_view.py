import numpy as np

a=np.array([1,2,3,4])
a1=a.copy()
a1[2]=5 # changing in copy of array doesn't change the original array
print(a)
print(a1)


a2=a.view()
a2[0]=5 #but changes in view array also changes in original array
print(a)
print(a2)
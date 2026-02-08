import numpy as np

x=np.array([1,2,3,4,5,6,7])
print(np.insert(x,4,9))
print()
print(np.append(x,6.5))

d=np.delete(x,4)
print(d)
import numpy as np

#shuffle
x=np.array([1,2,3,4,5,6,7,8])
print(np.random.shuffle(x))

#unique
print(np.unique(x))

#resize
print(np.resize(x,(2,3)))

#flatten
print(x.flatten(order='F')) #c:row major , F:column major ,A:column if continuos in memory,
#k:order the element occur

#ravel
print(np.ravel(x,order="K"))
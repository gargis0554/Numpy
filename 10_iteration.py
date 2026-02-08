import numpy as np
x=np.array([1,2,3,4])
for i in x:
    print(i)

print()
y=np.array([[1,2],[3,4]])
for i in y:
    for j in i:
        print(j)
print()
# using function
for i in np.nditer(x):
    print(i)
print()

for i,d in np.ndenumerate(x):
    print(i,d)
print()
for i in np.nditer(x,flags=["buffered"],op_dtypes=["float"]):
    print(i)

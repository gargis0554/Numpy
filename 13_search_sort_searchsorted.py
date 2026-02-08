import numpy as np
#search
x=np.array([1,2,3,5])
y=np.where(x==2)
print(y)

#search_sort array:binary search in the array : return the index where the 
# specified value would be inserted
z=np.searchsorted(x,4)
#(side="right"):index from right

#sorted
var=np.array([5,4,6,7,3,8,2,3,1])
print(np.sort(var))

#filter array
x = np.array([10, 25, 30, 45, 50])
filtered = x[x > 30]
print(filtered)


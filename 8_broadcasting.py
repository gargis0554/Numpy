import numpy as np

var1=np.array([1,2,3,4])
var2=np.array([1,2,3])

# both variable has diifferent no. of element
x=var1+var2  #x cannot be braodcasted 

#condition
#1.should be of same dimension
#2.(1x2)(3x1) moving from right left if one element is one in this 1 and 2 is there  :its valid and 
#and max of 1 and 3 is 3 :its makes additon possible
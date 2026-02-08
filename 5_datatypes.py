# bool_,int_,intc_,intp,int8,int16,int32,uint32,int64,float_,complex
import numpy as np

x=np.array([1,2,3,4])
print(x.dtype)

y=np.array([1,2,3,4],dtype='f')
print(y)
#or
#y=np.float32(x)

print(y.dtype)

#using astype function
x2=np.array([1,2,3,4])
new_1=x2.astype(float)
print(new_1)
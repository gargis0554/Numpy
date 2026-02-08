import numpy as np

var=np.random.rand(4) #between 0 and 1
print(var) #[0.0110494  0.74432011 0.99252574 0.48907496]

var1=np.random.randn(5) # close to 0 may return + and -
print(var1) #[-1.44715963  0.57894916  0.17595688 -0.22082861 -0.90266072]

var2=np.random.ranf(4) # 0<randf<1
print(var2) #[0.6766349  0.01322696 0.32700486 0.39809065]

var3=np.random.randint(5,100,10) #(min,max,no of elements)
print(var3) #[33 87 54 70 50 97 76 74 72 25]
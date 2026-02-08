import numpy as np

x=np.array([1,2,3,4])
y=np.array([5,6,7,8])

#add
add=np.add(x,y)
print(add) #[ 6  8 10 12]

#sub
sub=np.subtract(x,y)
print(sub) #[-4 -4 -4 -4]

#multiply
mul=np.multiply(x,y)
print(mul) #[ 5 12 21 32]

#divide
div=np.divide(x,y)
print(div) #[0.2        0.33333333 0.42857143 0.5       ]   

#mod
m=np.mod(x,y)
print(m) #[1 2 3 4]

#power
p=np.power(x,y)
print(p) #[    1    64  2187 65536]

#reciprocal
a=np.reciprocal(x)
print(a) #[1 0 0 0]

#min
b=np.min(x)
print(b) #1

#max
c=np.max(x)
print(c) #4

#argmin
d=np.argmin(x)
print(d) #0 position of min element

#sqrt
s=np.sqrt(x)
print(s) #[1.         1.41421356 1.73205081 2.        ]    

#sin
e=np.sin(x)
print(e) #[ 0.84147098  0.90929743  0.14112001 -0.7568025 ]

#cos
f=np.cos(x)
print(f) #[ 0.54030231 -0.41614684 -0.9899925  -0.65364362]

#cumsum
g=np.cumsum(x)
print(g) #[ 1  3  6 10]

#for 2d
var2=np.array([[1,2],[3,4]])
print(np.cumsum(var2)) #[ 1  3  6 10]
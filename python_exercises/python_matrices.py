import numpy as np
from numpy.linalg import inv

a = np.array([[1,2],[3,1]])

print (inv(a))

a = np.array([1,2])
b = np.array([4,3])
c = np.array([1,-1])
d = np.array([-1,100])
zip_list = (a,b)
sum = [a+b for (a,b) in zip_list]
dif = [a-b for (a,b) in zip_list]
prod = [a*b for (a,b) in zip_list]
quot = [a/b for (a,b) in zip_list]

print ("The sum of the two matrices are: ", sum)
print ("The difference of the two matrices are: ", dif)
print ("The product of the two matrices are: ", prod)
print ("The quotient of the two matrices are: ", quot)

c = np.array([[1,2,3],[-1,-3,-2],[1,0,1]])
d = np.array([[0,0,-1],[0,1,0],[1,0,-1]])

print(c)
print(d)

print (c+d)
print (d-c)
print (a/b)
print (c * d)
print(inv(d))
print(inv(c) * d)



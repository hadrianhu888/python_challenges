import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_power

a = np.array([[1,2],[3,1]])

print (a)
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

print(a)
print(b)
print(c)
print(d)

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
print(inv(c))
print(inv(c) * d)
print(np.dot(a,b))
print(np.cross(c,d))
print(inv(d) + inv(c))
print(matrix_power(c,3))
print(matrix_power(d,3))
print(np.eye(3))
print(np.swapaxes(np.eye(3),0,1))
print(np.transpose(c))

lst = list(input().split())

print(lst)




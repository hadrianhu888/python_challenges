import numpy as np

matrix_a = np.array([1,2], [3,4])
matrix_b = np.array([4,3], [-1.-2])

print ("The sum of the two matrices are: ")
print (np.add(matrix_a, matrix_b))

print ("The difference of the two matrices are: ")
print (np.subtract(matrix_a, matrix_b))

print ("The product of the two matrices are: ")
print (np.multiply(matrix_a, matrix_b))

print ("The division of the two matrices are: ")
print (np.divide(matrix_a, matrix_b))

print ("The dot product of the two matrices are: ")
print (np.dot(matrix_a, matrix_b))

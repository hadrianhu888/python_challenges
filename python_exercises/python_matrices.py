import numpy

matrix_a = numpy.array([1,2], [3,4])
matrix_b = numpy.array([4,3], [-1.-2])

print ("The sum of the two matrices are: ")
print (numpy.add(matrix_a, matrix_b))

print ("The difference of the two matrices are: ")
print (numpy.subtract(matrix_a, matrix_b))

print ("The product of the two matrices are: ")
print (numpy.prod(matrix_a, matrix_b))

print ("The division of the two matrices are: ")
print (numpy.divide(matrix_a, matrix_b))

print ("The dot product of the two matrices are: ")
print (numpy.dot(matrix_a, matrix_b))


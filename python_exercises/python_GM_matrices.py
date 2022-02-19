import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_power

matrix = np.array([[0,1],[1,2]])

print(matrix)

def SelCol (matrix, size, col, val):
    size = size - 1
    for i in range(size):
        matrix[col][i] = val
    print(matrix)
    
def SelRow (matrix, size, row, val):
    size = size - 1
    for i in range(size):
        matrix[i][row] = val
    print(matrix)

def QueryCol(matrix, size, row):
    size = size - 1
    row_sum = 0
    for i in range(size):
        matrix[row][i] = row_sum + matrix[row][i]
    print(matrix)
    print(row_sum)

def QueryCol(matrix, size, col):
    size = size - 1
    col_sum = 0
    for i in range(size):
        matrix[i][col] = col_sum + matrix[i][col]
    print(matrix)
    print(col_sum)

print(SelCol(matrix,2,1,3))
print(SelRow(matrix,2,0,4))
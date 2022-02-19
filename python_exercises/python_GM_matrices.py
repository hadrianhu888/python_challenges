import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_power

matrix = np.array([[0,1],[1,2]])

print(matrix)

def checkUserRowColInput(size,x):
    if x == size:
        return size - 1
    else:
        return x - 1

def SelCol (matrix, size, col, val):
    checkUserRowColInput(size, col) 
    for i in range(size):
        matrix[i][col] = val
    print(matrix)
    
def SelRow (matrix, size, row, val):
    checkUserRowColInput(size, row) 
    size = size - 1
    for i in range(size):
        matrix[row][i] = val
    print(matrix)

def QueryCol(matrix, size, row):
    checkUserRowColInput(size, row) 
    size = size - 1
    row_sum = 0
    for i in range(size):
        row_sum = row_sum + matrix[row][i]
    print(matrix)
    print(row_sum)

def QueryCol(matrix, size, col):
    checkUserRowColInput(size, col)
    size = size - 1
    col_sum = 0
    for i in range(size):
        col_sum = col_sum + matrix[i][col]
    print(matrix)
    print(col_sum)

def SelRowCol(matrix, size, row, col, val):
    checkUserRowColInput(size, col)
    checkUserRowColInput(size, row)
    for i in range(size):
        for j in range(size):
            matrix[row][col] = val
    print(matrix)
    
def findDiagonalSum(matrix, size):
    diag_sum = 0
    for i in range(size):
        for j in range(size):
            if (i == j):
                diag_sum = diag_sum + matrix[i][j]
            else: 
                diag_sum = 0
    print(matrix)
    print(diag_sum)
    return diag_sum

def findAntiDiagonalSum(matrix,size):
    anti_diag_sum = 0
    for i in range(size):
        for j in range(i):
            anti_diag_sum = anti_diag_sum + matrix[i][j]
    print(matrix)
    print(anti_diag_sum)
    return anti_diag_sum
    
print(SelCol(matrix,2,1,3))
print(SelRow(matrix,2,0,4))
print(SelRowCol(matrix,2,1,0,50))
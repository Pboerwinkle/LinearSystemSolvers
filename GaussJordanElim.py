import numpy as np
def elim(matrix, b):
    matrix=np.hstack((matrix, b.T))
    for row in range(len(matrix)):
        for row2 in range(row+1,len(matrix)):
            matrix[row2]=matrix[row2] - (matrix[row2][row]/matrix[row][row])*matrix[row]
    for row in range(len(matrix)-1,-1,-1):
        for row2 in range(row-1,-1,-1):
            matrix[row2]=matrix[row2] - (matrix[row2][row]/matrix[row][row])*matrix[row]
    for row in range(len(matrix)):
        matrix[row]/=matrix[row][row]
    return matrix
print(elim(np.array([[2,1,-1],[-3,-1,2],[-2,1,2.0]]), np.array([[8, -11, -3.0]])))

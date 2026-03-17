import numpy as np
matrix = np.array([[3,2,-1,1],[2,-2,4,-2],[-1,0.5,-1,0]])
def elim(matrix):
    for row in range(len(matrix)):
        for row2 in range(row+1,len(matrix)):
            matrix[row2]=matrix[row2] - (matrix[row2][row]/matrix[row][row])*matrix[row]
    for row in range(len(matrix)-1,-1,-1):
        for row2 in range(row-1,-1,-1):
            matrix[row2]=matrix[row2] - (matrix[row2][row]/matrix[row][row])*matrix[row]
    for row in range(len(matrix)):
        matrix[row]/=matrix[row][row]
    return matrix
print(elim(matrix))
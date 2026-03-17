import numpy as np
matrix = np.array([[3,2,-1,1],[2,-2,4,-2],[-1,0.5,-1,0]])
def decomp(matrix):
    def forwardSub(matrix, retL=False):
        multArray=np.zeros(np.shape(matrix))
        for row in range(len(matrix)):
            for row2 in range(row+1,len(matrix)):
                multiplier=(matrix[row2][row]/matrix[row][row])
                matrix[row2]=matrix[row2] - multiplier*matrix[row]
                multArray[row2][row]=multiplier
        for row in range(len(multArray)):
            multArray[row][row]=1
        if not retL:
            for row in range(len(matrix)):
                matrix[row]/=matrix[row][row]
        if retL:
            return matrix,multArray
        return matrix
    def backwardSub(matrix):
        for row in range(len(matrix)-1,-1,-1):
            for row2 in range(row-1,-1,-1):
                matrix[row2]=matrix[row2] - (matrix[row2][row]/matrix[row][row])*matrix[row]
        for row in range(len(matrix)):
            matrix[row]/=matrix[row][row]
        return matrix
    oldMatrix=matrix.copy()
    U,L=forwardSub(matrix, retL=True)
    for i in range(len(L)):
        L[i][-1]=oldMatrix[i][-1]
    print(L[:,:-1]@U[:,:-1])
    L=forwardSub(L)
    for i in range(len(U)):
        U[i][-1]=L[i][-1]
    results=backwardSub(U)
    return results
print(decomp(matrix))
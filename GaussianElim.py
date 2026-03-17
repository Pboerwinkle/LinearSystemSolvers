import numpy as np
def elim(matrix, mult=False):
    multArray=np.zeros(np.shape(matrix))
    for row in range(len(matrix)):
        for row2 in range(row+1,len(matrix)):
            multiplier=(matrix[row2][row]/matrix[row][row])
            matrix[row2]=matrix[row2] - multiplier*matrix[row]
            multArray[row2][row]=multiplier

    print(matrix)
    results=np.zeros(len(matrix))
    results[-1]=matrix[-1][-1]/matrix[-1][-2]
    for i in range(len(matrix)-2,-1,-1):
        s=0
        for j in range(i+1,len(matrix),1):
            s+=matrix[i][j]*results[j]
        results[i]=(matrix[i][-1]-s)/matrix[i][i]
    if mult:
        return results,multArray
    return results
print(elim(np.array([[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3.0]])))
import numpy as np
A = np.array([[3,2,-1],[2,-2,4],[-1,0.5,-1]])
b = np.array([1,-2,-0.0])
def cramer(A,b):
    def det(A):
        prod=1
        for row in range(len(A)):
            for row2 in range(row+1,len(A)):
                A[row2]=A[row2] - (A[row2][row]/A[row][row])*A[row]
            prod*=A[row][row]
        return prod
    detA=det(A.copy())
    results=np.zeros(np.shape(b))
    for i in range(len(b)):
        Ai=A.copy()
        Ai[:,i]=b
        results[i]=det(Ai)/det(A.copy())
    return results
print(cramer(A,b))
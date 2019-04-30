def matTrans(A):
    transA = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    return transA


# print(matTrans([[1, 2, 3], [4, 5, 6]]))
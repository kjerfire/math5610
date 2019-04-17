def vecOutProd(vector1, vector2):
    A = [[0 for i in range(len(vector2))] for j in range(len(vector1))]
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            A[i][j] = vector1[i] * vector2[j]
    return A


# TEST
mat1 = vecOutProd([1, 2, 3], [2, 3])

for i in range(len(mat1)):
    print(mat1[i])

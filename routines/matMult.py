def matMult(mat1, mat2):
    matTemp = [[0.0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(matTemp)):
        for j in range(len(matTemp[0])):
            temp = 0.0
            for k in range(len(mat1[0])):
                temp += mat1[i][k] * mat2[k][j]
            matTemp[i][j] = temp
    return matTemp


mat = matMult([[2, 0, 5], [5, 5, 5], [5, 7, 8], [1, 1, 1, ]], [[2, 2], [2, 2], [2, 2]])

for i in range(len(mat)):
    print(mat[i])
def matMult(mat1, mat2):
    matTemp = [[0.0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(matTemp)):
        for j in range(len(matTemp[0])):
            temp = 0.0
            for k in range(len(mat1[0])):
                temp += mat1[i][k] * mat2[k][j]
            matTemp[i][j] = temp
    return matTemp



# mat1 = [[1, 2], [2, 1], [1, 2]]
#
# mat2 = [[1, 2, 3], [3, 2, 1]]
#
# mat = matMult([[1, 2], [2, 1], [1, 2]], [[1, 2, 3], [3, 2, 1]])
#
# for i in range(len(mat)):
#     print(mat[i])
#
# for i in range(len(mat2)):
#     print(mat2[i])
#
# for i in range(len(mat1)):
#     print(mat1[i])
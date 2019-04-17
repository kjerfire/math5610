def matSum(matrix1, matrix2):
    A = [[0 for i in range(len(matrix1))] for j in range(len(matrix1[0]))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            A[i][j] = matrix1[i][j] + matrix2[i][j]
    return A


# TEST
# mat1 = matSum([[1, 2], [3, 4]], [[1, 2], [3, 4]])
#
# for i in range(len(mat1)):
#     print(mat1[i])

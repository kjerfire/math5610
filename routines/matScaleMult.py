def matScaleMult(matrix, multiplier):
    A = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            A[i][j] = multiplier * matrix[i][j]
    return A


# TEST


# mat1 = matScaleMult([[1, 2], [3, 4]], 5)
#
# for i in range(len(mat1)):
#     print(mat1[i])

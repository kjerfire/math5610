from vecAdd import *
from vecScale import *


def matRowEchForm(matrix):
    A = [[matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))]
    temp = [[matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            A[j] = vecAdd(temp[j], vecScale(temp[i], -temp[j][i] / temp[i][i]))
    for i in range(len(matrix)):
        A[i] = vecScale(A[i], 1 / A[i][i])
    return A


# TEST
# print(matRowEchForm([[1, 3, 5, 2], [2, 7, 3, 3], [4, 9, 8, 1]]))

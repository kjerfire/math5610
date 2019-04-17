from matRowEchForm import *
from matUpTriSolve import *

def matGE(matrix, b):
    for i in range(len(matrix)):
        matrix[i].append(b[i][0])
    # print(matrix)
    temp = matRowEchForm(matrix)
    for i in range(len(temp)):
        b[i][0] = temp[i].pop()
    # print(matrix)
    # print(temp)
    # print(b)
    soln = matUpTriSolve(temp, b)
    return soln


# TEST
# print(matGE([[1, 3, 5], [2, 7, 3], [4, 9, 8]], [[2], [3], [1]]))

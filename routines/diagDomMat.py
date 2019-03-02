import random

def diagDomMat(dimension):
    mat = [[random.random() for i in range(dimension)] for j in range(dimension)]
    for i in range(dimension):
        sum1 = 0
        for j in range(dimension):
            sum1 += abs(mat[i][j])
        mat[i][i] = sum1
    return mat


# mat = diagDomMat(3)
#
# for i in range(len(mat)):
#     print(mat[i])
#

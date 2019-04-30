from copy import deepcopy
from matMult import matMult



def matLUFact(mat):
    upper = deepcopy(mat)
    lower = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    for i in range(len(mat)):
        lower[i][i] = 1
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            lower[j][i] = upper[j][i] / upper[i][i]
            for k in range(i+1, len(mat)):
                upper[j][k] -= lower[j][i] * upper[i][k]
        for j in range(0, i):
            upper[i][j] = 0.0
    return [lower, upper]


# print(matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[0])
# print()
# print(matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[1])
# print()
# print(matMult(matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[0], matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[1]))

# HW 5 task 2 & 3
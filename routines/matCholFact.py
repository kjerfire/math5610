from matTrans import matTrans
from matMult import matMult

def matCholFact(mat):
    n = len(mat)
    lower = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(0, i):
            temp = mat[i][j]
            for k in range(0, j):
                temp -= lower[j][k] * lower[i][k]
            lower[i][j] = temp / lower[j][j]

        temp = mat[i][i]
        for j in range(0, i):
            temp -= pow(lower[i][j], 2)
        lower[i][i] = pow(temp, .5)
    return lower


# print(matCholFact([[4, 12, -16], [12, 37, -43], [-16, -43, 98]]))
#
#
# print(matMult(matCholFact([[4, 12, -16], [12, 37, -43], [-16, -43, 98]]),
#               matTrans(matCholFact([[4, 12, -16], [12, 37, -43], [-16, -43, 98]]))))


# HW 5 task 5
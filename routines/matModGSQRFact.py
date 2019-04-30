from matTrans import matTrans
from vecAdd import vecAdd
from vecScale import vecScale
from vecDotProduct import vecDotProduct
from vec2Norm import vec2Norm
from matMult import matMult


def matModGSQRFact(mat):
    uVec = matTrans(mat)
    # print(uVec)
    for i in range(len(mat[0])):
        for j in range(i):
            uVec[i] = vecAdd(uVec[i], vecScale(uVec[j], -1 * vecDotProduct(uVec[i], uVec[j])))
        # print(uVec)
        uVec[i] = vecScale(uVec[i], 1 / vec2Norm(uVec[i]))

    Q = [[uVec[i][j] for i in range(len(uVec))] for j in range(len(uVec[0]))]
    R = matMult(matTrans(Q), mat)

    return [Q, R]


# print(matModGSQRFact([[1, 2, 4], [0, 0, 5], [0, 3, 6]])[0])
# print()
# print(matModGSQRFact([[1, 2, 4], [0, 0, 5], [0, 3, 6]])[1])


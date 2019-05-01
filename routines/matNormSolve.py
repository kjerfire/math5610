from matTrans import matTrans
from matGE import matGE
from matMult import matMult


def matNormSolve(A, b):
    AtA = matMult(matTrans(A), A)
    Atb = matMult(matTrans(A), b)
    x = matGE(AtA, Atb)
    return x


print(matNormSolve([[2, -1], [1, 2], [1, 1]], [[2], [1], [4]]))
# HW 5 task 1
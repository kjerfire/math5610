from matTrans import matTrans
from matCholFact import matCholFact
from matMult import matMult
from matLowTriSolve import matLowTriSolve
from matUpTriSolve import matUpTriSolve


def matNormCholSolve(A, b):
    AtA = matMult(matTrans(A), A)
    Atb = matMult(matTrans(A), b)
    fact = matCholFact(AtA)
    solY = matLowTriSolve(fact, Atb)
    soln = matUpTriSolve(matTrans(fact), solY)
    return soln


# print(matNormCholSolve([[2, -1], [1, 2], [1, 1]], [[2], [1], [4]]))
# HW 5 task 6
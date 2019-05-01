from matTrans import matTrans
from matModGSQRFact import matModGSQRFact
from matMult import matMult
from matUpTriSolve import matUpTriSolve


def matLSQRSolve(A, b):
    fact = matModGSQRFact(A)
    solY = matMult(matTrans(fact[0]), b)
    soln = matUpTriSolve(fact[1], solY)
    return soln

# print(matLSQRSolve([[2, -1], [1, 2], [1, 1]], [[2], [1], [4]]))


# HW 6 Task 2

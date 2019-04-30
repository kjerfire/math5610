from matTrans import matTrans
from matModGSQRFact import matModGSQRFact
from matMult import matMult
from matUpTriSolve import matUpTriSolve


def matLSQRSolve(A, b):
    AtA = matMult(matTrans(A), A)
    Atb = matMult(matTrans(A), b)
    fact = matModGSQRFact(A)
    print(fact[0])
    print(fact[1])
    solY = matMult(matTrans(fact[0]), b)
    print(solY)
    soln = matUpTriSolve(fact[1], solY)
    return soln

print(matLSQRSolve([[2, -1], [1, 2], [1, 1]], [[2], [1], [4]]))


# HW 6 Task 2

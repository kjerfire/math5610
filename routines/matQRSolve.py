from matQRFact import matQRFact
from matUpTriSolve import matUpTriSolve
from matTrans import matTrans
from matMult import matMult

def matQRSolve(mat, b):
    QR = matQRFact(mat)
    solY = matMult(matTrans(QR[0]), b)
    soln = matUpTriSolve(QR[1], solY)
    return soln


print(matQRSolve([[1, 1, -1], [1, -2, 3], [2, 3, 1]], [[4], [-6], [7]]))

#  HW6 task 1
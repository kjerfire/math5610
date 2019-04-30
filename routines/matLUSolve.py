from matLUFact import matLUFact
from matLowTriSolve import matLowTriSolve
from matUpTriSolve import matUpTriSolve

def matLUSolve(mat, b):
    LU = matLUFact(mat)
    solY = matLowTriSolve(LU[0], b)
    soln = matUpTriSolve(LU[1], solY)
    return soln


print(matLUSolve([[1, 1, -1], [1, -2, 3], [2, 3, 1]], [[4], [-6], [7]]))

# HW 5 task 3
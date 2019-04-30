from matMult import matMult
from vecDotProduct import vecDotProduct
from vecScale import vecScale
from vecAdd import vecAdd
from vec2Norm import vec2Norm
from matScaleMult import matScaleMult
from copy import deepcopy

def gaussSeidel(A, b, x0, tol, maxiter, ct=False):
    x2 = deepcopy(x0)
    iter = 0
    error = 10 * tol
    while error > tol and iter < maxiter:
        x1 = deepcopy(x2)
        x2 = deepcopy(b)
        for i in range(len(A)):
            for j in range(i):
                x2[i][0] -= A[i][j] * x1[j][0]
            for j in range(i + 1, len(A)):
                x2[i][0] -= A[i][j] * x1[j][0]
            x2[i][0] /= A[i][i]
            x1[i][0] = x2[i][0]
        iter += 1
        error = vec2Norm(vecAdd(matMult(A, x2), vecScale(b, -1)))
    if ct == True:
        return x2, iter
    else:
        return x2


# print(gaussSeidel([[5, 1, 2], [1, 4, 1], [2, 2, 5]], [[1], [2], [3]], [[1], [2], [3]], .000001, 50))


# HW 6 task 7

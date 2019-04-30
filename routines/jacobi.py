from matMult import matMult
from vecScale import vecScale
from vecAdd import vecAdd
from vec2Norm import vec2Norm
from copy import deepcopy


def jacobi(A, b, x0, tol, maxiter, ct=False):
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
        for k in range(len(A)):
            x2[k][0] /= A[k][k]
        iter += 1
        error = vec2Norm(vecAdd(matMult(A, x2), vecScale(b, -1)))
    if ct == True:
        return x2, iter
    else:
        return x2


# print(jacobi([[5, 1, 2], [1, 4, 1], [2, 2, 5]], [[1], [2], [3]], [[1], [2], [3]], .00001, 50, True))

# HW 6 task 6
from matMult import matMult
from vecDotProduct import vecDotProduct
from vecScale import vecScale
from vecAdd import vecAdd
from vec2Norm import vec2Norm


def steepestDesc(A, b, x0, tol, maxiter, ct=False):
    error = 10.0 * tol
    iter = 0
    x = x0


    while error > tol and iter < maxiter:

        r = vecAdd(b, vecScale(matMult(A, x), -1))

        d1 = vecDotProduct(r, r)

        s = matMult(A, r)

        d2 = vecDotProduct(r, s)

        alpha = d1 / d2

        x = vecAdd(x, vecScale(r, alpha))

        iter += 1

        error = vec2Norm(r)
    if ct == True:
        return x, iter, error
    else:
        return x


# print(steepestDesc([[5, 1, 2], [1, 4, 1], [2, 2, 5]], [[1], [2], [3]], [[1], [2], [3]], .000001, 50))





from matMult import matMult
from vecDotProduct import vecDotProduct
from vecScale import vecScale
from vecAdd import vecAdd
from vec2Norm import vec2Norm
from matScaleMult import matScaleMult
from copy import deepcopy


def conGradient(A, b, x0, tol, maxiter, ct=False):
    r = vecAdd(b, matScaleMult(matMult(A, x0), -1))
    delta = vecDotProduct(r, r)
    iter = 0
    p = deepcopy(r)
    x = x0
    error = 10 * tol
    while error > tol and iter < maxiter:
        s = matMult(A, p)
        ak = delta / vecDotProduct(p, s)
        x = vecAdd(x, vecScale(p, ak))
        r = vecAdd(r, vecScale(s, -ak))
        delta1 = vecDotProduct(r, r)
        p = vecAdd(r, vecScale(p, (delta1 / delta)))
        delta = delta1
        iter += 1
        error = vec2Norm(r)
    if ct == True:
        return x, iter, error
    else:
        return x


print(conGradient([[5, 1, 2], [1, 4, 1], [2, 1, 5]], [[1], [2], [3]], [[1], [2], [3]], .000001, 10000))

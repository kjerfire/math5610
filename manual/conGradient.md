# Conjugate Gradient Solver 

**Routine Name:**           conGradient

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This program computes an iterative solution to a matrix by way of the conjugate gradient method.

**Input:** 
* Arguement 1: Matrix A
* Arguement 2: b vector
* Arguement 3: a guess vector
* Arguement 4: the error tolerance
* Arguement 5: the maximum allowable of iterations
* Arguement 6: a boolean option to iteration count and error

**Output:** This routine returns a solution vector. If arguement 6 is set to 'True', it will additionally output 
iteration count and error..

**Usage/Example:**

Below is a simple usage example solving a 3 by 3 matrix system:

```
print(conGradient([[5, 1, 2], [1, 4, 1], [2, 1, 5]], [[1], [2], [3]], [[1], [2], [3]], .000001, 10000))
```

Output from the lines above:

```
[[-0.10256410256410224], [0.38461538461538497], [0.5641025641025642]]
```

The above is the solution vector to the sample problem.

**Implementation/Code:** The following is the code for conGradient:

```
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
```

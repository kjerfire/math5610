# Steepest Descent Method Iterative Solver

**Routine Name:**           steepestDesc

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine implements the steepest descent method for iteratively solving systems of linear equations.

**Input:** 
* Arguement 1: Matrix A
* Arguement 2: b vector
* Arguement 3: a guess vector
* Arguement 4: the error tolerance
* Arguement 5: the maximum allowable of iterations
* Arguement 6: a boolean option to iteration count and error

**Output:** This routine returns a solution vector, and if called for the iteration and error.

**Usage/Example:**

Below is an example of a printed instance of the steepestDesc routine:

```
print(steepestDesc([[5, 1, 2], [1, 4, 1], [2, 2, 5]], [[1], [2], [3]], [[1], [2], [3]], .000001, 50))
```

Output from the lines above:

```
[[-0.06666658573339666], [0.4000000098691008], [0.466666617980326]]
```


**Implementation/Code:** The following is the code for steepestDesc:

```
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
```

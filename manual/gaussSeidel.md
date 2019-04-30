# Gauss Seidel Solver 

**Routine Name:**           gaussSeidel

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This program computes an iterative solution to a matrix by way of the Gauss Seidel method.

**Input:** 
* Arguement 1: Matrix A
* Arguement 2: b vector
* Arguement 3: a guess vector
* Arguement 4: the error tolerance
* Arguement 5: the maximum allowable of iterations
* Arguement 6: a boolean option to iteration count

**Output:** This routine returns a solution vector. If arguement 6 is set to 'True', it will additionally output 
iteration count.

**Usage/Example:**

Below is a simple usage example solving a 3 by 3 matrix system:

```
print(gaussSeidel([[5, 1, 2], [1, 4, 1], [2, 1, 5]], [[1], [2], [3]], [[1], [2], [3]], .000001, 10000))
```

Output from the lines above:

```
[[-0.10256410256410224], [0.38461538461538497], [0.5641025641025642]]
```

The above is the solution vector to the sample problem.

**Implementation/Code:** The following is the code for gaussSeidel:

```
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
```

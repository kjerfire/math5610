# Least Squares Q-R Factorization Solver

**Routine Name:**           matLSQRSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** Description

**Input:** 
* Arguement 1: matrix A
* Arguement 2: b vector

**Output:** This routine returns the least squares solution vector of the "Ax = b" system.

**Usage/Example:**

Below is an example of a printed instance of the matLSQRSolve routine:

```
print(matLSQRSolve([[2, -1], [1, 2], [1, 1]], [[2], [1], [4]]))
```

Output from the lines above:

```
[[1.4285714285714284], [0.4285714285714285]]
```

The above is least squares solution obtained from QR factorization, upper and lower triangular solving.

**Implementation/Code:** The following is the code for matLSQRSolve:

```
from matTrans import matTrans
from matModGSQRFact import matModGSQRFact
from matMult import matMult
from matUpTriSolve import matUpTriSolve


def matLSQRSolve(A, b):
    AtA = matMult(matTrans(A), A)
    Atb = matMult(matTrans(A), b)
    fact = matModGSQRFact(A)
    solY = matMult(matTrans(fact[0]), b)
    soln = matUpTriSolve(fact[1], solY)
    return soln
```

# Basic Least Squares Solver

**Routine Name:**           matNormSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine calculates a least squares solution with Gaussian Elimination.

**Input:** 
* Arguement 1: matrix A
* Arguement 2: b vector

**Output:** This routine returns the least squares solution vector of the "Ax = b" system.

**Usage/Example:**

Below is an example of a printed instance of the matNormSolve routine:

```
print(matNormSolve([[2, -1], [1, 2], [1, 1]], [[2], [1], [4]]))
```

Output from the lines above:

```
[[1.4285714285714286], [0.4285714285714286]]
```

The above is least squares solution obtained from QR factorization, upper and lower triangular solving.

**Implementation/Code:** The following is the code for matNormSolve:

```
from matTrans import matTrans
from matGE import matGE
from matMult import matMult


def matNormSolve(A, b):
    AtA = matMult(matTrans(A), A)
    Atb = matMult(matTrans(A), b)
    x = matGE(AtA, Atb)
    return x
```

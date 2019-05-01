# QR Factorization Solver

**Routine Name:**           matQRSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** Description

**Input:** 
* Arguement 1: matrix A
* Arguement 2: b vector

**Output:** This routine decomposes the input matrix into QR parts, and then solves by backward and forward substitution.

**Usage/Example:**

Below is an example of a printed instance of the matQRSolve routine:

```
print(matQRSolve([[1, 1, -1], [1, -2, 3], [2, 3, 1]], [[4], [-6], [7]]))
```

Output from the lines above:

```
[[1.0000000000000002], [2.0], [-1.0000000000000002]]
```

Note that the solution to the matrix is (1, 2, -1), but finite machine precision limits the accuracy just a touch.

**Implementation/Code:** The following is the code for matQRSolve:

```
from matQRFact import matQRFact
from matUpTriSolve import matUpTriSolve
from matTrans import matTrans
from matMult import matMult

def matQRSolve(mat, b):
    QR = matQRFact(mat)
    solY = matMult(matTrans(QR[0]), b)
    soln = matUpTriSolve(QR[1], solY)
    return soln
```

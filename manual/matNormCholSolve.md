# Least Squares Cholesky Factorization Solver

**Routine Name:**           matNormCholSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:**  This routine computes the least squares solution of the "Ax = b" system via the Cholesky Factorization.

**Input:** 
* Arguement 1: matrix A
* Arguement 2: b vector

**Output:** This routine returns least squares solution vector.

**Usage/Example:**

Below is an example of a printed instance of the matNormCholSolve routine:

```
print(matNormCholSolve([[2, -1], [1, 2], [1, 1]], [[2], [1], [4]]))
```

Output from the lines above:

```
[[1.4285714285714286], [0.42857142857142855]]
```


**Implementation/Code:** The following is the code for matNormCholSolve:

```
from matTrans import matTrans
from matCholFact import matCholFact
from matMult import matMult
from matLowTriSolve import matLowTriSolve
from matUpTriSolve import matUpTriSolve


def matNormCholSolve(A, b):
    AtA = matMult(matTrans(A), A)
    Atb = matMult(matTrans(A), b)
    fact = matCholFact(AtA)
    solY = matLowTriSolve(fact, Atb)
    soln = matUpTriSolve(matTrans(fact), solY)
    return soln
```

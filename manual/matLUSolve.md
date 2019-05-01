# LU Factorization Solver

**Routine Name:**           matLUSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** Description

**Input:** 
* Arguement 1: matrix A
* Arguement 2: b vector

**Output:** This routine returns the solution vectorof a matrix A by LU factorization and forward and back substitution.

**Usage/Example:**

Below is an example of a printed instance of the matLUSolve routine:

```
print(matLUSolve([[1, 1, -1], [1, -2, 3], [2, 3, 1]], [[4], [-6], [7]]))
```

Output from the lines above:

```
[[1.0], [2.0], [-1.0]]
```

In this case, the routine is able to find an exact solution.

**Implementation/Code:** The following is the code for matLUSolve:

```
from matLUFact import matLUFact
from matLowTriSolve import matLowTriSolve
from matUpTriSolve import matUpTriSolve

def matLUSolve(mat, b):
    LU = matLUFact(mat)
    solY = matLowTriSolve(LU[0], b)
    soln = matUpTriSolve(LU[1], solY)
    return soln
```

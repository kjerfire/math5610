# Title  Lower Triangular Matrix Solver

**Routine Name:**           matLowTriSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** Description

**Input:** 
* Arguement 1: lower triangular matrix
* Arguement 2: b vector

**Output:** This routine returns a the solution vector of of a linear system with a lower triangular matrix.

**Usage/Example:**

Below is an example of a printed instance of the matLowTriSolve routine:

```
print(matLowTriSolve([[-2, 0, 0, 0, 0], [4, 9, 0, 0, 0], [2, 3, 2, 0, 0], [3, 2, 4, 3, 0], [1, 5, 5, 6, 4]],
                    [[1], [2], [3], [4], [5]]))
```

Output from the lines above:

```
[[-0.5], [0.4444444444444444], [1.3333333333333335], [-0.24074074074074092], [-0.48611111111111116]]

```

The output is the printed solution vector.

**Implementation/Code:** The following is the code for matLowTriSolve:

```
def matLowTriSolve(matrix, b):
    xSoln = [0 for i in range(len(b))]
    for i in range(len(matrix)):
        for j in reversed(range(i)):
            b[i][0] = b[i][0] - matrix[i][j] * xSoln[j]
        xSoln[i] = b[i][0] / matrix[i][i]
    soln = [[0] for i in range(len(xSoln))]
    for i in range(len(soln)):
        soln[i][0] = xSoln[i]
    return soln

```

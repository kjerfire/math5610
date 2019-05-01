# Title  Upper Triangular Matrix Solver

**Routine Name:**           matUpTriSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** Description

**Input:** 
* Arguement 1: upper triangular matrix
* Arguement 2: b vector

**Output:** This routine returns a the solution vector of of a linear system with an upper triangular matrix.

**Usage/Example:**

Below is an example of a printed instance of the matUpTriSolve routine:

```
print(matUpTriSolve([[1, 5, 5, 6, 4], [0, 3, 4, 2, 3], [0, 0, 2, 3, 1], [0, 0, 0, 9, 4], [0, 0, 0, 0, -2]],
                    [[1], [2], [3], [4], [5]]))
```

Output from the lines above:

```
[[-8.287037037037038], [1.5740740740740744], [0.4166666666666665], [1.5555555555555556], [-2.5]]

```

The output is the printed solution vector.

**Implementation/Code:** The following is the code for matUpTriSolve:

```
def matUpTriSolve(matrix, b):
    xSoln = [0 for i in range(len(b))]
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(i + 1, len(matrix)):
            b[i][0] = b[i][0] - matrix[i][j] * xSoln[j]
        xSoln[i] = b[i][0] / matrix[i][i]
    soln = [[0] for i in range(len(xSoln))]
    for i in range(len(soln)):
        soln[i][0] = xSoln[i]
    return soln

```

# Diagonal Matrix Solver

**Routine Name:**           matDiagSolve

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute the solution to a linear system where "A" is a diagonal matrix.

**Input:** 
* Arguement 1: diagonal matrix
* Arguement 2: b vector

**Output:** This routine returns a vector of length n where n is the dimension of the square diagolnal input matrix.

**Usage/Example:**

The program returns the solution vector. Following is an example of the code:

```
print(matDiagSolve([[5, 0, 0], [0, 10, 0], [0, 0, 125]], [[1], [2], [25]]))
```

Output from the lines above:

```
[5.0, 5.0, 5.0]
```

This vector is the result when each element of the matrix is divided by the corresponding value of the b vector.

**Implementation/Code:** The following is the code for matDiagSolve:

```
def matDiagSolve(matrix, b):
    xSoln = [0 for i in range(len(b))]
    for i in range(len(matrix)):
        xSoln[i] = matrix[i][i] / b[i][0]
    return xSoln
```

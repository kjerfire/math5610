#  LU Factorization

**Routine Name:**           matLUFact

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** Description

**Input:** 
* Arguement 1: matrix


**Output:** This routine returns two matrices which constitute the LU decomposition of the original matrix.

**Usage/Example:**

Below is an example of the matLUFact routine, run three times:

```
print(matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[0])
print()
print(matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[1])
print()
print(matMult(matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[0], matLUFact([[1, 1, -1], [1, -2, 3], [2, 3, 1]])[1]))

```

Output from the lines above:

```
[[1, 0, 0], [1.0, 1, 0], [2.0, -0.3333333333333333, 1]]

[[1, 1, -1], [0.0, -3.0, 4.0], [0.0, 0.0, 4.333333333333333]]

[[1.0, 1.0, -1.0], [1.0, -2.0, 3.0], [2.0, 3.0, 1.0]]

```

The first prints the L matrix, the second prints the U matrix, and the third multiplies LU to obtain the original matrix.

**Implementation/Code:** The following is the code for matLUFact:

```
from copy import deepcopy
from matMult import matMult



def matLUFact(mat):
    upper = deepcopy(mat)
    lower = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    for i in range(len(mat)):
        lower[i][i] = 1
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            lower[j][i] = upper[j][i] / upper[i][i]
            for k in range(i+1, len(mat)):
                upper[j][k] -= lower[j][i] * upper[i][k]
        for j in range(0, i):
            upper[i][j] = 0.0
    return [lower, upper]
```

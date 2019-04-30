# Title Cholesky Factorization

**Routine Name:**           matCholFact

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine generates the lower triangular decomposed part of the the Cholesky Factorization.

**Input:** 
* Arguement 1: matrix


**Output:** This routine returns a lower triangle matrix that when multiplied by its transpose, returns the original matrix.

**Usage/Example:**

Below are two examples the first of the factored loer part, and the second is the back multiplication by the transpose:

```
print(matCholFact([[4, 12, -16], [12, 37, -43], [-16, -43, 98]]))


print(matMult(matCholFact([[4, 12, -16], [12, 37, -43], [-16, -43, 98]]), 
  matTrans(matCholFact([[4, 12, -16], [12, 37, -43], [-16, -43, 98]]))))


```

Output from the lines above:

```
[[2.0, 0, 0], [6.0, 1.0, 0], [-8.0, 5.0, 3.0]]
[[4.0, 12.0, -16.0], [12.0, 37.0, -43.0], [-16.0, -43.0, 98.0]]
```

The frist line is the factored matrix. The second line is the origional matrix.

**Implementation/Code:** The following is the code for matChollFact:

```
from matTrans import matTrans
from matMult import matMult

def matCholFact(mat):
    n = len(mat)
    lower = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(0, i):
            temp = mat[i][j]
            for k in range(0, j):
                temp -= lower[j][k] * lower[i][k]
            lower[i][j] = temp / lower[j][j]

        temp = mat[i][i]
        for j in range(0, i):
            temp -= pow(lower[i][j], 2)
        lower[i][i] = pow(temp, .5)
    return lower

```

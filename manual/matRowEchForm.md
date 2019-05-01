# Row Echelon Form Transformer

**Routine Name:**           matRowEchForm

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine transforms the input matrix into upper triangular row echelon form.

**Input:** 
* Arguement 1: matrix

**Output:** This routine returns an equivalent matrix to the input matrix, but transforms it into Row Echelon Form.

**Usage/Example:**

Below is an example of a printed instance of the matRowEchForm routine:

```
print(matRowEchForm([[1, 3, 5, 2], [2, 7, 3, 3], [4, 9, 8, 1]]))
```

Output from the lines above:

```
[[1.0, 3.0, 5.0, 2.0], [0.0, 1.0, -7.0, -1.0], [0.3448275862068966, 0.0, 1.0, -0.6896551724137934]]
```

Note that this particular implementation is additionally reduced row echelon form, with the diagonal entries all equal to 1.

**Implementation/Code:** The following is the code for matRowEchForm:

```
from vecAdd import *
from vecScale import *


def matRowEchForm(matrix):
    A = [[matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))]
    temp = [[matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            A[j] = vecAdd(temp[j], vecScale(temp[i], -temp[j][i] / temp[i][i]))
    for i in range(len(matrix)):
        A[i] = vecScale(A[i], 1 / A[i][i])
    return A
```

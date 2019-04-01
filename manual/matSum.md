# Matrix Addition Calculator

**Routine Name:**           matSum

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute the sum of two matrices with the same dimensions.

**Input:** 
* Arguement 1: matrix 1
* Arguement 2: matrix 2

**Output:** This routine returns a matirx of dimension m by n with each element i, j equal to matrix1[i][j] + matrix2[i][j].

**Usage/Example:**

The program returns the summed matrix. Following is an example of the code:

```
mat1 = matSum([[1, 2], [3, 4]], [[1, 2], [3, 4]])

for i in range(len(mat1)):
    print(mat1[i])
```

Output from the lines above:

```
[2, 4]
[6, 8]
```

This matrix is the  sum of the 2 by 2 matrices.

**Implementation/Code:** The following is the code for matMult:

```
def matSum(matrix1, matrix2):
    A = [[0 for i in range(len(matrix1))] for j in range(len(matrix1[0]))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            A[i][j] = matrix1[i][j] + matrix2[i][j]
    return A

```

# Matrix Scalar Multiplication Calculator

**Routine Name:**           matScaleMult

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute product of a matrix with a scale value.

**Input:** 
* Arguement 1: a matrix 
* Arguement 2: a number

**Output:** This routine returns a matirx of dimension m by n with evey entry multiplied by the scale number.

**Usage/Example:**

The program returns the scaled matrix. Following is an example of the code:

```
mat1 = matScaleMult([[1, 2], [3, 4]], 5)

for i in range(len(mat1)):
    print(mat1[i])
```

Output from the lines above:

```
[5, 10]
[15, 20]
```

This matrix is the product of the 2 by 2 matrix and the scalar number 5.

**Implementation/Code:** The following is the code for matScaleMult:

```
def matScaleMult(matrix, multiplier):
    A = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            A[i][j] = multiplier * matrix[i][j]
    return A
```

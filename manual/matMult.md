# Matrix Multiplication Calculator

**Routine Name:**           matMult

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute  product of two matrices with the same inner dimension.

**Input:** 
* Arguement 1: matrix 1
* Arguement 2: matrix 2

**Output:** This routine returns a matirx of dimension m by n where m is the number of rows of matrix 1, and n is 
the number of columns of matrix 2..

**Usage/Example:**

The program returns the product matrix. Following is an example of the code:

```
mat1 = matMult([[1, 2], [2, 1], [1, 2]], [[1, 2, 3], [3, 2, 1]])

for i in range(len(mat1)):
    print(mat1[i])
```

Output from the lines above:

```
[7.0, 6.0, 5.0]
[5.0, 6.0, 7.0]
[7.0, 6.0, 5.0]
```

This matrix is the  product of the 3 by 2 and 2 by 3 matrices.

**Implementation/Code:** The following is the code for matMult:

```
def matMult(mat1, mat2):
    matTemp = [[0.0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(matTemp)):
        for j in range(len(matTemp[0])):
            temp = 0.0
            for k in range(len(mat1[0])):
                temp += mat1[i][k] * mat2[k][j]
            matTemp[i][j] = temp
    return matTemp
```

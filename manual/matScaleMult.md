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

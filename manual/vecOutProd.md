# Vector Outer Product Calculator

**Routine Name:**           vecOutProd

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute the outer product of two input vectors.

**Input:** 
* Arguement 1: vector 1
* Arguement 2: vector 2

**Output:** This routine returns a matirx of dimension m by n where m is the length of vector 1, and n is 
the length of vector 2.

**Usage/Example:**

The program returns the product matrix. Following is an example of the code:

```
mat1 = vecOutProd([1, 2, 3], [2, 3])

for i in range(len(mat1)):
    print(mat1[i])
```

Output from the lines above:

```
[2, 3]
[4, 6]
[6, 9]

```

This matrix is the  product of the 3 length, and 2 length vectors. Note that with the outer product, if the input vectors 
were switched, the dimensions of the output matrix would also be switched

**Implementation/Code:** The following is the code for matMult:

```
def vecOutProd(vector1, vector2):
    A = [[0 for i in range(len(vector2))] for j in range(len(vector1))]
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            A[i][j] = vector1[i] * vector2[j]
    return A
```

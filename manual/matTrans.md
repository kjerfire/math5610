# Matrix Transposer

**Routine Name:**           matTrans

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine transposes an input matrix.

**Input:** 
* Arguement 1: matrix

**Output:** A single matrix.

**Usage/Example:**

Below is an example of a printed instance of the matTrans routine:

```
print(matTrans([[1, 2, 3], [4, 5, 6]]))
```

Output from the lines above:

```
[[1, 4], [2, 5], [3, 6]]
```

Note that in this non square matrix the dimension was m by n and is now n by m.

**Implementation/Code:** The following is the code for matTrans:

```
def matTrans(A):
    transA = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    return transA
```

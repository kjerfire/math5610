# Modified Graham-Schmidt QR Factorization

**Routine Name:**           matModGSQRFact

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine decomposes an input matrix into two component matrices in the QR form by the Modified Graham-Schmidt process.

**Input:** 
* Arguement 1:  matrix

**Output:** This routine returns two matrices in a python set.

**Usage/Example:**

Below is an example of a printed usage instance of the matModGSQRFact routine:

```
print(matModGSQRFact([[1, 2, 4], [0, 0, 5], [0, 3, 6]])[0])
print()
print(matModGSQRFact([[1, 2, 4], [0, 0, 5], [0, 3, 6]])[1])
```

Output from the lines above:

```
[[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]

[[1.0, 2.0, 4.0], [0.0, 3.0, 6.0], [0.0, 0.0, 5.0]]

```

Note that the first print is indexing the first matrix of the set and the second prints the other.

**Implementation/Code:** The following is the code for matModGSQRFact:

```
from matTrans import matTrans
from vecAdd import vecAdd
from vecScale import vecScale
from vecDotProduct import vecDotProduct
from vec2Norm import vec2Norm
from matMult import matMult


def matModGSQRFact(mat):
    uVec = matTrans(mat)
    for i in range(len(mat[0])):
        for j in range(i):
            uVec[i] = vecAdd(uVec[i], vecScale(uVec[j], -1 * vecDotProduct(uVec[i], uVec[j])))
        uVec[i] = vecScale(uVec[i], 1 / vec2Norm(uVec[i]))

    Q = [[uVec[i][j] for i in range(len(uVec))] for j in range(len(uVec[0]))]
    R = matMult(matTrans(Q), mat)

    return [Q, R]
```

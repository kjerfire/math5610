#  QR Factorization

**Routine Name:**           matQRFact

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** Description

**Input:** 
* Arguement 1: matrix

**Output:** This routine returns two matrices which constitute the QR decomposition of the input matrix.


**Usage/Example:**

Below is an example of the matQRFact routine, run two times:

```
print(matQRFact([[1, 2, 4], [0, 0, 5], [0, 3, 6]])[0])
print()
print(matQRFact([[1, 2, 4], [0, 0, 5], [0, 3, 6]])[1])
```

Output from the lines above:

```
[[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]

[[1.0, 2.0, 4.0], [0.0, 3.0, 6.0], [0.0, 0.0, 5.0]]

```

The first prints the Q matrix, the second prints the R matrix.

**Implementation/Code:** The following is the code for matQRFact:

```
from matTrans import matTrans
from vecAdd import vecAdd
from vecScale import vecScale
from vecDotProduct import vecDotProduct
from vec2Norm import vec2Norm
from matMult import matMult


def matQRFact(mat):
    columns = matTrans(mat)
    uVec = matTrans(mat)
    # print(uVec)
    for i in range(len(mat)):
        for j in range(i):
            uVec[i] = vecAdd(uVec[i], vecScale(uVec[j], -1 * vecDotProduct(columns[i], uVec[j])))
        # print(uVec)
        uVec[i] = vecScale(uVec[i], 1 / vec2Norm(uVec[i]))

    Q = [[uVec[i][j] for i in range(len(uVec))] for j in range(len(uVec[0]))]
    R = matMult(matTrans(Q), mat)

    return [Q, R]

```

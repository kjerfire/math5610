# Random Symmetric Positive Definite Matrix Generator

**Routine Name:**           symmPosDefMat

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This routine will generate a symmetric positive definite matrix with random values of the 
dimensions input by a user. 

**Input:** 
* Arguement 1: One integer value.

**Output:** The return is a matrix.

**Usage/Example:**

Below is an example of a printed instance of the symmPosDefMat routine:

```
mat = symmPosDefMat(4)
for i in range(len(mat)):
    print(mat[i])
```        

Output from the lines above:

```
[4, 0.40365195386414265, 0.10826322578069558, 0.011541285081796082]
[0.40365195386414265, 4, 0.6133551923205521, 0.6499349416790732]
[0.10826322578069558, 0.6133551923205521, 4, 0.5321975223556581]
[0.011541285081796082, 0.6499349416790732, 0.5321975223556581, 4]
```

**Implementation/Code:** The following is the code for symmPosDefMat()

```
import random


def symmPosDefMat(n):
    blank = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            blank[i][j] = random.random()
            blank[j][i] = blank[i][j]
    for i in range(n):
        blank[i][i] = n
    return blank
```

[Back to Manual](README.md)

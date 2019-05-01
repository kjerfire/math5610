# Random Symmetric Positive Definite Generator

**Routine Name:**           symmDiagDom

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This routine will generate a symmetric positive definite matrix with random values of the 
dimensions input by a user. 

**Input:** 
* Arguement 1: One integer value.

**Output:** The return is a matrix.

**Usage/Example:**

Below is an example of a printed instance of the symmDiagDom routine with:

```
mat = symmDiagDom(4)
for i in range(len(mat)):
    print(mat[i])
```        

Output from the lines above:

```
[4, 0.6332981307957046, 0.021014114809406736, 0.9026259152268065]
[0.6332981307957046, 4, 0.9173093809467656, 0.22489937942836657]
[0.021014114809406736, 0.9173093809467656, 4, 0.900728683121824]
[0.9026259152268065, 0.22489937942836657, 0.900728683121824, 4]
```

**Implementation/Code:** The following is the code for symmDiagDom:

```
import random

def symmDiagDom(n):
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

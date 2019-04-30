# Gaussian Elimination

**Routine Name:**           matGE

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This program is a simple linear system solver which uses Gaussian Elimination.

**Input:** 
* Arguement 1: matrix A
* Arguement 2: b vector

**Output:** This routine returns the solution vector to the input linear system.

**Usage/Example:**

The following is code showing the use of the matGE routine for a 3 by 3 matrix:

```
print(matGE([[1, 3, 5], [2, 7, 3], [4, 9, 8]], [[2], [3], [1]]))
```

Output from the lines above:

```
[[22.931034482758626], [-5.827586206896553], [-0.6896551724137934]]
```

This vector is the solution to the input system.

**Implementation/Code:** The following is the code for matGE:

```
from matRowEchForm import *
from matUpTriSolve import *

def matGE(matrix, b):
    for i in range(len(matrix)):
        matrix[i].append(b[i][0])
    temp = matRowEchForm(matrix)
    for i in range(len(temp)):
        b[i][0] = temp[i].pop()
    soln = matUpTriSolve(temp, b)
    return soln
```

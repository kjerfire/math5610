# Random Diagonally Dominant Matrix Generator

**Routine Name:**           diagDomMat

**Author:** Nathanael Barney

**Language:** Python 3.7.


**Description/Purpose:** This routine will generate a square matrix with the property of diagonal dominance.

**Input:** 
* Arguement: an integer, the dimension of the square matrix.

**Output:** The return is an n by n diagonally dominant matrix.

**Usage/Example:**

This program a single integer entry,the n of the desired n by n matrix. Following is an example of the program usage:

```
mat = diagDomMat(3)

for i in range(len(mat)):
    print(mat[i])
```

Output from the lines above:

```
[0.9447495010451202, 0.3741843425526523, 0.5436645457817622]
[0.5571612831619189, 1.949835814047987, 0.39529384730177497]
[0.9446992520564044, 0.1361787184830493, 1.4700290763330695]
```

**Implementation/Code:** The following is the code for diagDomMat
import random

def diagDomMat(dimension):

```
    mat = [[random.random() for i in range(dimension)] for j in range(dimension)]
    for i in range(dimension):
        sum1 = 0
        for j in range(dimension):
            sum1 += abs(mat[i][j])
        mat[i][i] = sum1
    return mat
    
```    

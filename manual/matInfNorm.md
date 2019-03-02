# Matrix Infinity Norm Calculator

**Routine Name:**           matInfNorm

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program calculates the infinity norm of a matrix. 

**Input:** 
* Arguement 1: a single matrix

**Output:** The program returns a single number, the infinity norm of the input matrix.

**Usage/Example:**

An example of usage of the matInfNorm function:

```
print(matInfNorm([[5, 5, 10], [1, 1, 1], [9, 8, 7]]))
```

Output from the lines above:

```
 24 
```

**Implementation/Code:** The following is the code for vecInfNorm

```
def matInfNorm(mat):
    tempList = []
    for i in range(len(mat)):
        temp = 0
        for j in range(len(mat[i])):
            temp += abs(mat[i][j])
        tempList.append(temp)
    return max(tempList)
```

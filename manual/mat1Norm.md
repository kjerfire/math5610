# Matrix 1 Norm Calculator

**Routine Name:**           mat1Norm

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program calculates the 1 norm of a matrix. 

**Input:** 
* Arguement 1: a single matrix

**Output:** The program returns a single number, the 1 norm of the input matrix.

**Usage/Example:**

An example of usage of the vec1Norm function:

```
print(mat1Norm([[5, 5, 10], [1, 1, 1], [9, 8, 7]]))
```

Output from the lines above:

``` 18 ```

**Implementation/Code:** The following is the code for vec1Norm

```
def mat1Norm(mat):
    tempList = []
    for j in range(len(mat)):
        temp = 0
        for i in range(len(mat[j])):
            temp += abs(mat[i][j])
        tempList.append(temp)
    return max(tempList)
```

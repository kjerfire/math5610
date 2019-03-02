# Vector Dot Product Calculator

**Routine Name:**           vecDotProduct

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute the cross product of two vectors, that being matrix that 
results from vector multiplication.

**Input:** 
* Arguement 1: vector 1
* Arguement 2: vector 2

**Output:** This routine returns a cross product matrix of dimension m by n where m is the number of values 
in vector 1, and n is the number of entries in vector 2.

**Usage/Example:**

The routine returns the single dot product value. Following is an example of the code:

```
 print(vecCrossProduct([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
 
for i in range(len(mat)):
    print(mat[i])
 ```

Output from the lines above:

```
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
[4, 8, 12, 16, 20]
[5, 10, 15, 20, 25]
```

This value is the cross product of the vectors [1, 2, 3, 4, 5], and [1, 2, 3, 4, 5].

**Implementation/Code:** The following is the code for vecCrossProduct

```
def vecCrossProduct(vec1, vec2):
    crossMatrix = [[] for i in range(len(vec1))]
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            crossMatrix[i].append(vec1[i] * vec2[j])
    return crossMatrix
```

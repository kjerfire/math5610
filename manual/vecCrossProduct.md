# Vector Cross Product Calculator

**Routine Name:**           vecCrossProduct

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute the cross product of two vectors, returning the vector that 
results from such an operation.

**Input:** 
* Arguement 1: vector 1
* Arguement 2: vector 2

**Output:** This routine returns a cross product matrix of dimension m by n where m is the number of values 
in vector 1, and n is the number of entries in vector 2.

**Usage/Example:**

The routine returns the cross product vector. Following is an example of the code:

```
vec = vecCrossProduct([1, 2, 3], [-1, 7, 26])

print(vec)
 ```

Output from the lines above:

```
[46, -6, 5]
```

This value is the cross product of the vectors [1, 2, 3], and [-1, 7, 26].

**Implementation/Code:** The following is the code for vecCrossProduct

```
def vecCrossProduct(vec1, vec2):
    crossProd = [[] for i in range(3)]
    crossProd[0] = vec1[1] * vec2[2] - vec1[2] * vec1[1]
    crossProd[1] = vec1[2] * vec2[0] - vec1[0] * vec1[2]
    crossProd[2] = vec1[0] * vec2[1] - vec1[1] * vec1[0]
    return crossProd
```

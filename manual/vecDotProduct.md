# Vector Dot Product Calculator

**Routine Name:**           vecDotProduct

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This routine will compute the dot product of two vectors, that being the 
sum of element-wise multiplication of two vectors of equal length.

**Input:** 
* Arguement 1: a vector
* Arguement 2: a vector of the same length

**Output:** This routine returns a single number, the dot product.

**Usage/Example:**

The routine returns the single dot product value. Following is an example of the code:

```
 print(vecDotProduct([1, 1, 1, 1, ], [2, 3, 4, 5]))
 ```

Output from the lines above:

```
 14.0 
```

This value is the dot product of the vectors [1, 1, 1, 1, ], and [2, 3, 4, 5].

**Implementation/Code:** The following is the code for vecDotProduct

```
def vecDotProduct(vec1, vec2):
    dot = 0.0
    for i in range(len(vec1)):
        temp = vec1[i] * vec2[i]
        dot += temp
    return dot
```

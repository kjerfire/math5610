# Vector Infinity-Norm Error

**Routine Name:**           vecInfNormError

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program calculates the absolute error of a vector approximation when the Infinity-norm is used. 

**Input:** 
* Arguement 1: A vector of the actual value 
* Arguement 2: A vector of the approximate value


**Output:** The program returns a single number, the absolute error of the infinity norm.

**Usage/Example:**

An example of usage of the vecInfNormError function:

      list1 = [1.75, 1.9, 2.9, 4.2]
      list2 = [2, 2, 3, 4]
      print(vecInfNormError(list1, list2))


Output from the lines above:

      0.25


**Implementation/Code:** The following is the code for vecInfNormError.

```
def vecInfNormError(actual, approx):
  vec = actual[:]
  vecApprox = approx[:]
  for i in range(len(vec)):
    vec[i] -= vecApprox[i]
  for i in range(len(vec)):
    vec[i] = abs(vec[i])
  return max(vec)
```


[Back to Manual](README.md)

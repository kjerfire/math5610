# Vector 2 Norm Error

**Routine Name:**           vec2NormError

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program calculates the absolute error of a vector approximation when the 2-norm is used. 

**Input:** Two numeric vectors, the exact vector and the approximate vector.

**Output:** The program returns a single number, the absolute error.

**Usage/Example:**

An example of usage of the vec1NormError function:

      list1 = [1.75, 1.9, 2.9, 4.2]
      list2 = [2, 2, 3, 4]
      print(vec1NormError(list1, list2))


Output from the lines above:

      0.35000000000000014

The returned number is the absolute error in terms of the vector 2-norm.

**Implementation/Code:** The following is the code for vec2NormError.

      def vec1NormError(actual, approx):
        vec = actual[:]
        vecApprox = approx[:]
        for i in range(len(vec)):
          vec[i] -= vecApprox[i]
        for i in range(len(vec)):
          vec[i] = vec[i] ** 2
        sum = 0
        for i in range(len(vec)):
          sum += vec[i]
        return sum ** .5


[Back to Manual](README.md)

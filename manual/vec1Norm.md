# Vector 1 Norm Calculator

**Routine Name:**           vec1Norm

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program calculates the 1 norm of a vector by taking the sum of the absolute value of the elements. 

**Input:** One numeric list object(vector).

**Output:** The program returns a single number, the 1 norm of the input vector.

**Usage/Example:**

An example of usage of the vecAdd function:

      print(vec1Norm([6, 8, 12]))

Output from the lines above:

      26

The returned number is the 1 norm of the [6, 8, 12] vector.

**Implementation/Code:** The following is the code for vec1Norm

      def vec1Norm(vec):
        norm = 0
        for i in range(len(vec)):
          norm += abs((vec[i] ** 1))
        return norm ** 1

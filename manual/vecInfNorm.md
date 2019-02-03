# Vector Infinity Norm Calculator

**Routine Name:**           vecInfNorm

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program calculates the infinity norm of a vector by identifying the element of greatest magnitude. 

**Input:** One numeric list object(vector).

**Output:** The program returns a single number, the infinity norm of the input vector.

**Usage/Example:**

An example of usage of the vecInfNorm function:

      print(vecInfNorm([6, 8, 12]))

Output from the lines above:

      12

The returned number is the 2 norm of the [6, 8, 12] vector.

**Implementation/Code:** The following is the code for vecInfNorm

      def vecInfNorm(vec):
        norm = 0
        test = 0
        for i in range(len(vec)):
          if test < abs(vec[i]):
            norm = abs(vec[i])
        return norm


[Back to Manual](README.md)

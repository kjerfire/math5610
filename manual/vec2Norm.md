# Vector 2 Norm Calculator

**Routine Name:**           vec2Norm

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program calculates the 2 norm of a vector by taking the square root of the sum of squared elements. 

**Input:** One numeric list object(vector).

**Output:** The program returns a single number, the 2 norm of the input vector.

**Usage/Example:**

An example of usage of the vecAdd function:

      print(vec2Norm([6, 8, 12]))

Output from the lines above:

      15.620499351813308

The returned number is the 2 norm of the [6, 8, 12] vector.

**Implementation/Code:** The following is the code for vecAdd

      def vec2Norm(vec):
        norm = 0
        for i in range(len(vec)):
          norm += (vec[i] ** 2)
        return norm ** .5

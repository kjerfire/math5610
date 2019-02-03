# Random Symmetric Matrix Generator

**Routine Name:**           symmMat

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This routine will generate a two dimensional list with random values of the n by n dimensions input by a user. 
The object generated will have a symmetric structure where the the following holds true:

      matrix[i][j] == matrix[j][i]

**Input:** One integer value.

**Output:** The return is a python list object, with lists as elements (matrix).

**Usage/Example:**

This program takes one integer entries representing the n dimension of the matrix, in the case below, 5 * 5. 
The following test code stores the output of symmMat, and then prints row by row.

      mat = symmMat(5)
      
      for i in range(len(mat)):
        print(mat[i])


Output from the lines above:

      [0.7500573961901216, 0.0003922260219531015, 0.8548924844743049, 0.40481315003215734, 0.908476171629602]
      [0.0003922260219531015, 0.7215772321778774, 0.3566808794028554, 0.9036660182414211, 0.2194523798805046]
      [0.8548924844743049, 0.3566808794028554, 0.09149928973648358, 0.03698338285112013, 0.130178766081385]
      [0.40481315003215734, 0.9036660182414211, 0.03698338285112013, 0.9950248691098137, 0.6961470586627319]
      [0.908476171629602, 0.2194523798805046, 0.130178766081385, 0.6961470586627319, 0.9473083519591448]



**Implementation/Code:** The following is the code for smaceps()

      import random
      
      
      def symmMat(n):
        blank = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
          for j in range(i, n):
            blank[i][j] = random.random()
            blank[j][i] = blank[i][j]
        return blank

[Back to Manual](README.md)

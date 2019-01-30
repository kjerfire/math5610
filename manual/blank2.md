# Random Matrix Generator

**Routine Name:**           randMat

**Author:** Nathanael Barney

**Language:** Python. The code can be run in the Python language.


**Description/Purpose:** This routine will generate a two dimensional list with random values of the dimensions input by a user.

**Input:** The inputs required are two integer values. The first parameter indicating m, or thr number of rows, and the second being n or the number of columns in the matrix.

**Output:** The return is a python list object, with lists as elements.

**Usage/Example:**

This program takes two integer entries representing the m * n matrix, in the case below, 5 * 3. The following test code stores the output of randMat, and then prints row by row.

      mat = randMat(5, 3)
      
      for i in range(len(mat)):
        print(mat[i])

Output from the lines above:

      [0.4938284270187818, 0.10448299040645204, 0.4420265505920872]
      [0.7863414356559334, 0.7378855988792082, 0.8705942473156126]
      [0.52600107842278, 0.4423276246551957, 0.5885647467926489]
      [0.4780078559236475, 0.8675458914501607, 0.317085150320899]
      [0.32392693889319746, 0.1861545569256703, 0.553129086642555]


**Implementation/Code:** The following is the code for smaceps()

      import random
      
      
      def randMat(m, n):
        return [[random.random() for i in range(n)] for j in range(m)]
      



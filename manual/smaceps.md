# Single Precision Calculator

**Routine Name:**           smaceps

**Author:** Nathanael Barney

**Language:** Python. The code can be run using the Python Language.

**Description/Purpose:** This routine will compute the single precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run only one time for each computer.

**Input:** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

The routine returns two values in a list each representative of a different aspect of machine precision. The first is an integer representing the number of bits used to store the floating point number, and the second is the floating point number of maximum precision.

      x1 = smaceps()
      
      print("Single float mantissa: " + str(x1[0]))
      print("Single float precision: " + str(x1[1]))

Output from the lines above:

      Single float mantissa: 24
      Single float precision: 5.9604645e-08


**Implementation/Code:** The following is the code for smaceps()

      import numpy as np
      
      
      def smaceps():
        one = np.float32(1.0)
        seps = np.float32(1.0)
        appone = one + seps
      
      ipow = 0
      
        while one != appone:
            ipow += 1
            seps /= np.float32(2)
            appone = one + seps
        
        return [ipow, seps]

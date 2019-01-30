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

The routine has two arguments needed to return the values of the precision in terms of the smallest number that can be
represented. Since the code is written in terms of a Fortran subroutine, the values of the machine machine epsilon and
the power of two that gives the machine epsilon. Due to implicit Fortran typing, the first argument is a single precision
value and the second is an integer.

      x1 = smaceps()
      
      print("Double float mantissa: " + str(x1[0]))
      print("Double float precision: " + str(x1[1]))

Output from the lines above:

      Double float mantissa: 24
      Double float precision: 5.9604645e-08

The first value (24) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-08 on the
end of the second value).

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

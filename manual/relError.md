# Relative Error

**Routine Name:**           relError

**Author:** Nathanael Barney

**Language:** Python 3.7.


**Description/Purpose:** This program calculates the proportionate difference between two numbers, providing a relative error value of a number, and its estimate.

**Input:** The program accepts two parameters, an origional value, and the estimate.

**Output:** The program returns a single positive number.

**Usage/Example:**

The example below shows the program calculating the error of the estimate 13 from the value 13.00041.

      print(relError(.000000008, .00000001))

Output from the lines above:

      0.24999999999999994



**Implementation/Code:** The following is the code for relError

      def absError(num1, num2):
        error = abs(num1-num2)
        return error


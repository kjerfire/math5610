# Absolute Error

**Routine Name:**           absError

**Author:** Nathanael Barney

**Language:** Python 3.7.


**Description/Purpose:** This program calculates the positive distance between two numbers, providing an error value of a number, and its estimate.

**Input:** The program accepts two parameters, an origional value, and the estimate.

**Output:** The program returns a single positive number.

**Usage/Example:**

The example below shows the program calculating the error of the estimate 13 from the value 13.00041.

      print(absError(13.00041, 13))

Output from the lines above:

      0.000410000000001247



**Implementation/Code:** The following is the code for smaceps()

      def absError(num1, num2):
        error = abs(num1-num2)
        return error


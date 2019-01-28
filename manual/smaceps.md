# Single Precision Calculator

**Routine Name:**           smaceps

**Author:** Nathanael Barney

**Language:** Python. 

For example,

    smaceps.py

will run the program.

**Description/Purpose:** This routine will compute the single precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run only one time for each computer.

**Input:** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

**Output:** This routine prints a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

This code displays two values representing precision. Firstly the machine epsilon and second the
the power of two that gives the machine epsilon. 

      smaceps()

What is then displayed upon excecuting the line above:

      24   5.96046448E-08

The first value (24) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-08 on the
end of the second value).

**Implementation/Code:** The following is the code for smaceps()

      subroutine smaceps(seps, ipow)

# Vector Scaling

**Routine Name:**           vecScale

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program multiplies every element of a numeric list by a number, as vector scaling by a constant. 

**Input:** One numeric list object(vector), and a number.

**Output:** The program returns a single numeric list.

**Usage/Example:**

An example of usage of the vecScale function:

      print(vecScale([1, 2, 3, 4], 5))

Output from the lines above:

      [5, 10, 15, 20]


The returned list is the multiplication of each element, by 5.

**Implementation/Code:** The following is the code for vecScale

      def vecScale(vec, scale):
        for i in range(len(vec)):
            vec[i] *= scale
        return vec


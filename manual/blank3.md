# Vector Addition

**Routine Name:**           vecAdd

**Author:** Nathanael Barney

**Language:** Python 3.7

**Description/Purpose:** This program adds numeric list objects element-wise, as vector addition. 

**Input:** Two numeric list objects(vectors).

**Output:** The program returns a single numeric list.

**Usage/Example:**

An example of usage of the vecAdd function:

      vec = vecAdd([1, 2, 3, 4], [1, 2, 3, 4])
      
      print(vec)

Output from the lines above:

      [2, 4, 6, 8]


The returned list is the addition of elements, by position.

**Implementation/Code:** The following is the code for vecAdd

      def vecAdd(vec1, vec2):
        for i in range(len(vec1)):
            vec1[i] += vec2[i]
        return vec1

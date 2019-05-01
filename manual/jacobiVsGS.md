# Jacobi VS Gauss Seidel

**Routine Name:**           jacobiVsGS

**Author:** Nathanael Barney

**Language:** Python 3.7.

**Description/Purpose:** This program presents a back and forth comparison of the Jacobi iteration and Gauss Seidel solving methods.

**Input:** 
* No input is required

**Output:** This routine prints basic information about the nature of how the methods solved the randomly generated input matrices.

**Usage/Example:**

Below is an example of a printed instance of the jacobiVsGS routine:

```
jacobiVsGS()
```

Output from the lines above:

```
A matrix of size 10 by 10 takes Jacobi's method 0.003988027572631836 seconds to converge after 17 iterations.
A matrix of size 10 by 10 takes the Gauss-Seidel method 0.0009975433349609375 seconds to converge after 6 iterations.
A matrix of size 25 by 25 takes Jacobi's method 0.014957904815673828 seconds to converge after 20 iterations.
A matrix of size 25 by 25 takes the Gauss-Seidel method 0.00498652458190918 seconds to converge after 7 iterations.
A matrix of size 70 by 70 takes Jacobi's method 0.0937509536743164 seconds to converge after 24 iterations.
A matrix of size 70 by 70 takes the Gauss-Seidel method 0.02991795539855957 seconds to converge after 8 iterations.
A matrix of size 100 by 100 takes Jacobi's method 0.1815204620361328 seconds to converge after 24 iterations.
A matrix of size 100 by 100 takes the Gauss-Seidel method 0.07679200172424316 seconds to converge after 8 iterations.
A matrix of size 500 by 500 takes Jacobi's method 4.586731433868408 seconds to converge after 28 iterations.
A matrix of size 500 by 500 takes the Gauss-Seidel method 1.380338191986084 seconds to converge after 9 iterations.
A matrix of size 1000 by 1000 takes Jacobi's method 20.940016269683838 seconds to converge after 29 iterations.
A matrix of size 1000 by 1000 takes the Gauss-Seidel method 6.749945402145386 seconds to converge after 10 iterations.
```

As we can clearly see, the Gauss-Seidel method is markedly faster than Jacobi, how neat.

**Implementation/Code:** The following is the code for blank:

```
import time
from symmPosDefMat import symmPosDefMat
from jacobi import jacobi
from gaussSeidel import gaussSeidel

def jacobiVsGS():
    for i in [10, 25, 70, 100, 500, 1000]:
        mat = symmPosDefMat(i)
        vec = [[1] for j in range(i)]
        time0 = time.time()
        x, count = jacobi(mat, vec, vec, .0001, 10000, True)
        print("A matrix of size " + str(i) + " by " + str(i) + " takes Jacobi's method " + str(time.time() - time0) +
              " seconds to converge after " + str(count) + " iterations.")
        time1 = time.time()
        x, count = gaussSeidel(mat, vec, vec, .0001, 10000, True)
        print("A matrix of size " + str(i) + " by " + str(i) + " takes the Gauss-Seidel method " +
              str(time.time() - time1) + " seconds to converge after " + str(count) + " iterations.")
```

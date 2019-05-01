from conGradient import conGradient
from steepestDesc import steepestDesc
import time

def hilbertSDTest():
    for k in [4, 8, 16, 32]:
        hilberti = [[1 / (1 + i + j) for i in range(k)] for j in range(k)]
        vec = [[1] for j in range(k)]
        time0 = time.time()
        x, count, error = steepestDesc(hilberti, vec, vec, .001, 100000, True)
        print("A Hilbert matrix of size " + str(k) + " by " + str(k) + " takes the Steepest Descent method " +
              str(time.time() - time0) + " seconds to converge after " + str(count) + " iterations with an error of " +
               str(error))


hilbertSDTest()
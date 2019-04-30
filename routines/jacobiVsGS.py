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





# methodCompare()
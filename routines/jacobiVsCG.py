import time
from symmPosDefMat import symmPosDefMat
from jacobi import jacobi
from conGradient import conGradient







def jacobiVsCG():
    for i in [10, 25, 70, 100, 500]:
        mat = symmPosDefMat(i)
        vec = [[1] for j in range(i)]
        time0 = time.time()
        x, count = jacobi(mat, vec, vec, .0001, 10000, True)
        print("A matrix of size " + str(i) + " by " + str(i) + " takes Jacobi's method " + str(time.time() - time0) +
              " seconds to converge after " + str(count) + " iterations.")
        time1 = time.time()
        x, count, error = conGradient(mat, vec, vec, .0001, 10000, True)
        print("A matrix of size " + str(i) + " by " + str(i) + " takes the Conjugate Gradient method " +
              str(time.time() - time1) + " seconds to converge after " + str(count) + " iterations.")
    return

jacobiVsCG()





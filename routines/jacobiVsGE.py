import time
from symmPosDefMat import symmPosDefMat
from jacobi import jacobi
from matGE import matGE

def jacobiVsGE():
    for i in [10, 25, 70, 100, 500]:
        mat = symmPosDefMat(i)
        vec = [[1] for j in range(i)]
        time0 = time.time()
        x, count = jacobi(mat, vec, vec, .0001, 10000, True)
        print("A matrix of size " + str(i) + " by " + str(i) + " takes Jacobi's method " + str(time.time() - time0) +
              " seconds to converge after " + str(count) + " iterations.")
        time1 = time.time()
        x = matGE(mat, vec)
        print("A matrix of size " + str(i) + " by " + str(i) + " takes the Gaussian Elimination method " +
              str(time.time() - time1) + " seconds to solve.")



jacobiVsGE()
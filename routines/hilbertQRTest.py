from matQRSolve import matQRSolve
from matQRFact import matQRFact
from matTrans import matTrans
from matMult import matMult
import time

def hilbertQRTest():
    for k in [4, 8, 16, 32]:
        hilberti = [[1 / (1 + i + j) for i in range(k)] for j in range(k)]
        if k == 4:
            hilbertQ, hilbertR = matQRFact(hilberti)
            identity = matMult(matTrans(hilbertQ), hilbertQ)
        vec = [[1] for j in range(k)]
        time0 = time.time()
        x = matQRSolve(hilberti, vec)
        print("A Hilbert matrix of size " + str(k) + " by " + str(k) + " takes the QR method " +
              str(time.time() - time0) + " seconds to solve.")
        print()
    print("Note that for the 4 by 4 matrix the QtQ is roughly equal to the identity:")
    print()
    for i in range(len(identity)):
        print(identity[i])

hilbertQRTest()
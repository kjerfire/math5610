import numpy as np


def smaceps():
    one = np.float32(1.0)
    seps = np.float32(1.0)
    appone = one + seps

    ipow = 0

    while one != appone:
        ipow += 1
        seps /= np.float32(2)
        appone = one + seps

    print(str(ipow))
    print("Single float mantissa: " + str(seps))

smaceps()

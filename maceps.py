def maceps():
    one = 1.0
    seps = 1.0
    appone = one + seps

    ipow = 0

    while one != appone:
        ipow += 1
        seps /= 2
        appone = one + seps

    print(str(ipow))
    print("Double float mantissa: " + str(seps))

maceps()

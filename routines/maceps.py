def maceps():
    one = 1.0
    seps = 1.0
    appone = one + seps

    ipow = 0

    while one != appone:
        ipow += 1
        seps /= 2
        appone = one + seps

    return [ipow, seps]


x1 = maceps()

print("Double float mantissa: " + str(x1[0]))
print("Double float precision: " + str(x1[1]))


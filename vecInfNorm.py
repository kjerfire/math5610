def vecInfNorm(vec):
    norm = 0
    test = 0
    for i in range(len(vec)):
        if test < abs(vec[i]):
            norm = abs(vec[i])
    return norm


print(vecInfNorm([6, 8, 12]))

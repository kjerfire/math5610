def vec1NormError(actual, approx):
    vec = actual[:]
    vecApprox = approx[:]
    for i in range(len(vec)):
        vec[i] -= vecApprox[i]
    for i in range(len(vec)):
        vec[i] = abs(vec[i])
    sum = 0
    for i in range(len(vec)):
        sum += vec[i]
    return sum

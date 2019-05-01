def vecInfNormError(actual, approx):
    vec = actual[:]
    vecApprox = approx[:]
    for i in range(len(vec)):
        vec[i] -= vecApprox[i]
    for i in range(len(vec)):
        vec[i] = abs(vec[i])
    return max(vec)


# list1 = [1.75, 1.9, 2.9, 4.2]
# list2 = [2, 2, 3, 4]
# print(vecInfNormError(list1, list2))
#

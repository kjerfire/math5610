def vec1Norm(vec):
    norm = 0
    for i in range(len(vec)):
        norm += abs((vec[i] ** 1))
    return norm ** 1


print(vec1Norm([6, 8, 12]))
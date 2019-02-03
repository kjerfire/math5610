def vec2Norm(vec):
    norm = 0
    for i in range(len(vec)):
        norm += (vec[i] ** 2)
    return norm ** .5



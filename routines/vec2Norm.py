def vec2Norm(vec):
    norm = 0
    if isinstance(vec[0], int) or isinstance(vec[0], float):
        for i in range(len(vec)):
            norm += (vec[i] ** 2)
        return norm ** .5

    for i in range(len(vec)):
        norm += (vec[i][0] ** 2)
    return norm ** .5


# print((vec2Norm([[5], [4], [3], [1]])))
# print(vec2Norm([5, 4, 3, 1]))
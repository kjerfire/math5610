def vecDotProduct(vec1, vec2):
    dot = 0.0
    if isinstance(vec1[0], int) or isinstance(vec1[0], float):
        for i in range(len(vec1)):
            temp = vec1[i]* vec2[i]
            dot += temp
        return dot
    for i in range(len(vec1)):
        temp = vec1[i][0] * vec2[i][0]
        dot += temp
    return dot


# print(vecDotProduct([[1], [1], [1], [1]], [[2], [3], [4], [5]]))

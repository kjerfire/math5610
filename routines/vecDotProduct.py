def vecDotProduct(vec1, vec2):
    dot = 0.0
    for i in range(len(vec1)):
        temp = vec1[i] * vec2[i]
        dot += temp
    return dot


# print(vecDotProduct([1, 1, 1, 1], [2, 3, 4, 5]))
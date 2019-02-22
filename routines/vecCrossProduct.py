def vecCrossProduct(vec1, vec2):
    crossMatrix = [[] for i in range(len(vec1))]
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            crossMatrix[i].append(vec1[i] * vec2[j])
    return crossMatrix


mat = vecCrossProduct([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, ])

for i in range(len(mat)):
    print(mat[i])
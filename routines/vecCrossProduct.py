def vecCrossProduct(vec1, vec2):
    crossProd = [[] for i in range(3)]
    crossProd[0] = vec1[1] * vec2[2] - vec1[2] * vec1[1]
    crossProd[1] = vec1[2] * vec2[0] - vec1[0] * vec1[2]
    crossProd[2] = vec1[0] * vec2[1] - vec1[1] * vec1[0]
    return crossProd


# mat = vecCrossProduct([1, 2, 3], [-1, 7, 26])
#
# for i in range(len(mat)):
#     print(mat[i])

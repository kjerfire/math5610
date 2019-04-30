from copy import deepcopy

def vecAdd(vec1, vec2):
    if isinstance(vec1[0], int) or isinstance(vec1[0], float):
        vecTemp = [vec1[i] for i in range(len(vec1))]
        for i in range(len(vec1)):
            vecTemp[i] += vec2[i]
        return vecTemp

    vecTemp1 = deepcopy(vec1)
    vecTemp2 = deepcopy(vec2)
    for i in range(len(vecTemp1)):
        vecTemp1[i][0] += vecTemp2[i][0]
    return vecTemp1


# print(type([[5], [4], [3], [1]][0]))
# print(type([5, 4, 3, 1][0]))
# print((vecAdd([[5], [4], [3], [1]], [[5], [4], [3], [1]])))
# print(vecAdd([5, 4, 3, 1], [5, 4, 3, 1]))

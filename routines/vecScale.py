from copy import deepcopy


def vecScale(vec, scale):
    if isinstance(vec[0], int) or isinstance(vec[0], float):
        vecTemp = [vec[i] for i in range(len(vec))]
        for i in range(len(vec)):
            vecTemp[i] *= scale
        return vecTemp
    vecTemp = deepcopy(vec)
    for i in range(len(vec)):
        vecTemp[i][0] *= scale
    return vecTemp


# print(vecScale([1,2,2], -3))
# print(vecScale([[1],[2],[2]], -3))
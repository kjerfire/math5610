def vecScale(vec, scale):
    for i in range(len(vec)):
        vec[i] *= scale
    return vec


print(vecScale([1, 2, 3, 4], 5))


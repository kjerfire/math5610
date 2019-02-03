import random


def randMat(m, n):
    return [[random.random() for i in range(n)] for j in range(m)]


mat = randMat(5, 3)

for i in range(len(mat)):
    print(mat[i])



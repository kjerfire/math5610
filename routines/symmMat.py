import random


def symmMat(n):
    blank = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            blank[i][j] = random.random()
            blank[j][i] = blank[i][j]
    return blank


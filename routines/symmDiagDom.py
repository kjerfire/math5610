import random

def symmDiagDom(n):
    blank = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            blank[i][j] = random.random()
            blank[j][i] = blank[i][j]
    for i in range(n):
        blank[i][i] = n
    return blank

# mat = symmDiagDom(4)
# for i in range(len(mat)):
#     print(mat[i])
def matrix(x, y):
    return [[0 for i in range(y)] for j in range(x)]


mat1 = Matrix(5, 4)

print(mat1)

mat1[4][3] = 11

print(mat1)
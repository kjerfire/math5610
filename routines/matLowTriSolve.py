def matLowTriSolve(matrix, b):
    xSoln = [0 for i in range(len(b))]
    for i in range(len(matrix)):
        for j in reversed(range(i)):
            b[i][0] = b[i][0] - matrix[i][j] * xSoln[j]
        xSoln[i] = b[i][0] / matrix[i][i]
    soln = [[0] for i in range(len(xSoln))]
    # print(soln)
    # print(xSoln)
    for i in range(len(soln)):
        soln[i][0] = xSoln[i]
    return soln


# TEST
# print(matLowTriSolve([[-2, 0, 0, 0, 0], [4, 9, 0, 0, 0], [2, 3, 2, 0, 0], [3, 2, 4, 3, 0], [1, 5, 5, 6, 4]],
#                     [[1], [2], [3], [4], [5]]))
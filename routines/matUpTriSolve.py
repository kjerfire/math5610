def matUpTriSolve(matrix, b):
    xSoln = [0 for i in range(len(b))]
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(i + 1, len(matrix)):
            b[i][0] = b[i][0] - matrix[i][j] * xSoln[j]
        xSoln[i] = b[i][0] / matrix[i][i]
    soln = [[0] for i in range(len(xSoln))]
    for i in range(len(soln)):
        soln[i][0] = xSoln[i]
    return soln


# # TEST
print(matUpTriSolve([[1, 5, 5, 6, 4], [0, 3, 4, 2, 3], [0, 0, 2, 3, 1], [0, 0, 0, 9, 4], [0, 0, 0, 0, -2]],
                    [[1], [2], [3], [4], [5]]))


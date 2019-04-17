def matDiagSolve(matrix, b):
    xSoln = [0 for i in range(len(b))]
    for i in range(len(matrix)):
        xSoln[i] = matrix[i][i] / b[i][0]
    return xSoln


# # TEST
print(matDiagSolve([[5, 0, 0], [0, 10, 0], [0, 0, 125]], [[1], [2], [25]]))

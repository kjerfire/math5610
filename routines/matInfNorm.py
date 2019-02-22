def matInfNorm(mat):
    tempList = []
    for i in range(len(mat)):
        temp = 0
        for j in range(len(mat[i])):
            temp += abs(mat[i][j])
        tempList.append(temp)
    return max(tempList)


print(matInfNorm([[1, 1, 20], [1, -10, 50], [5, 10, 15]]))
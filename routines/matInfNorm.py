def matInfNorm(mat):
    tempList = []
    for i in range(len(mat)):
        temp = 0
        for j in range(len(mat[i])):
            temp += abs(mat[i][j])
        tempList.append(temp)
    return max(tempList)


print(matInfNorm([[5, 5, 10], [1, 1, 1], [9, 8, 7]]))
def mat1Norm(mat):
    tempList = []
    for j in range(len(mat)):
        temp = 0
        for i in range(len(mat[j])):
            temp += abs(mat[i][j])
        tempList.append(temp)
    return max(tempList)


# print(mat1Norm([[5, 5, 10], [1, 1, 1], [9, 8, 7]]))
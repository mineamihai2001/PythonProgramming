def matrix_replace(matrix:list[list]) -> list[list]:
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            if i > j: matrix[i][j] = 0

matrix = [[1, 1, 1], [1, 1, 1],[1, 1, 1]]
matrix_replace(matrix)
print(matrix)
def can_see(matrix):
    columns = list()
    result = list()
    for i in range(len(matrix)):
        column = list()
        for j in range(len(matrix[0])):
            column.append(matrix[i][j])
        columns.append(column)
    for column in columns:
        for i in range(len(column)):
            if column[i] >


def matrix_input():
    rows = list(
        input("Enter the rows in a single line (separate rows by \",\"):  ").split(","))
    rows_counter = len(rows)

    matrix = []
    for row in rows:
        column = list(row.split())
        if (rows_counter != len(column)):
            return None
        matrix.append(column)
    return matrix


def spiral(matrix):
    left = 0
    result = ""
    c = r = len(matrix)
    right = c - 1
    top = 0
    bottom = r - 1
    while left <= right and top <= bottom:

        for i in range(left, right + 1):
            result+=str(matrix[top][i])
        top += 1

        for i in range(top, bottom - 1, -1):
            result+=str(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result+=str(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result+=str(matrix[i][left])
            left += 1
    return result


matrix = matrix_input()
if matrix == None:
    print("Invalid input, the matrix needs to be square")
    exit
result_string = spiral(matrix)

print(result_string)

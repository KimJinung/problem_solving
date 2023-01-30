def solution(rows, columns, queries):
    answer = []

    matrix = generate_matrix(rows, columns)

    for query in queries:
        row1, col1, row2, col2 = map(lambda x: x - 1, query)

        min_value, matrix = rotate_matrix(matrix, row1, col1, row2, col2)

        answer.append(min_value)

    return answer


def generate_matrix(rows, cols) -> list:
    return [
        [num for num in range(row, row + cols)]
        for row in range(1, rows * cols + 1, cols)
    ]


def rotate_matrix(
    matrix: list, row1: int, col1: int, row2: int, col2: int
) -> (int, list):
    row, col = row1, col1

    is_row = False
    is_negative = False

    prev_value = matrix[row][col]
    min_value = prev_value

    while True:
        if not is_row:
            if not is_negative:
                col += 1
            else:
                col -= 1
        else:
            if not is_negative:
                row += 1
            else:
                row -= 1

        current_value = matrix[row][col]

        matrix[row][col] = prev_value

        prev_value = current_value

        if prev_value < min_value:
            min_value = prev_value

        if (col == col1 or col == col2) and (row == row1 or row == row2):
            is_row = not is_row

        if row == row2 and col == col2:
            is_negative = True

        if row == row1 and col == col1:
            break

    return min_value, matrix

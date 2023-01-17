# 풀이과정 리뷰 한 번 더 하기 - 2023.01.17.
def solution(m, n, board):
    board = [list(x) for x in board]

    matched_dots = True

    while matched_dots:
        matched_dots = []

        for row in range(m - 1):
            for col in range(n - 1):
                if (
                    board[row][col]
                    == board[row][col + 1]
                    == board[row + 1][col]
                    == board[row + 1][col + 1]
                    != "@"
                ):
                    matched_dots.append((row, col))

        for row, col in matched_dots:
            board[row][col] = board[row][col + 1] = board[row + 1][col] = board[
                row + 1
            ][col + 1] = "@"

        for row in range(m - 1):
            for col in range(n):
                if board[row + 1][col] == "@":
                    board[row + 1][col], board[row][col] = board[row][col], "@"

    return sum(row.count("@") for row in board)

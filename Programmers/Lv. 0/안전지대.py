def solution(board):
    length = len(board)

    coord_of_bomb = set()

    for x, row in enumerate(board):
        for y, _ in enumerate(row):
            if not board[x][y]:
                continue

            coord_of_bomb.update(
                (x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]
            )

    return length * length - sum(
        0 <= x < length and 0 <= y < length for x, y in coord_of_bomb
    )

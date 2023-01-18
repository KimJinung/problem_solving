from collections import deque


def solution(maps):
    row = len(maps)
    col = len(maps[0])

    q = deque([(0, 0, 1)])

    while q:
        x, y, depth = q.popleft()

        if maps[x][y] == 1 or maps[x][y] > depth:
            maps[x][y] = depth

            for next_x, next_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dx, dy = x + next_x, y + next_y

                if 0 <= dx <= row - 1 and 0 <= dy <= col - 1 and maps[dx][dy] != 0:
                    q.append((dx, dy, depth + 1))

    answer = maps[row - 1][col - 1]

    return -1 if answer == 1 else answer

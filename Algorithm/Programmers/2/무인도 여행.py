"""
문제가 요구하는 것
- 2차원 배열에서 상, 하, 좌, 우로 연결되어 있는 각 그룹의 인자 합

사용할 알고리즘
- Depth First Search

아이디어
- 2차원 배열을 순회하면서 DFS를 재귀적으로 태운다.
- 각 결과를 별도로 저장한다.
"""


def solution(maps):
    answer = []

    maps = [list(row) for row in maps]

    row_size = len(maps)
    col_size = len(maps[0])

    def _dfs(x_dot: int, y_dot: int) -> int:
        if not maps[x_dot][y_dot].isdigit():
            return 0

        result = 0

        stack = [[x_dot, y_dot]]

        while stack:
            x, y = stack.pop()

            if maps[x][y].isdigit():
                result += int(maps[x][y])

                maps[x][y] = "X"

                for dx, dy in get_all_directions_dots(x, y):
                    if 0 <= dx < row_size and 0 <= dy < col_size:
                        stack.append([dx, dy])

        return result

    for x, row in enumerate(maps):
        for y, period in enumerate(row):
            if period.isdigit():
                if length_of_stay := _dfs(x, y):
                    answer.append(length_of_stay)

    if answer:
        return sorted(answer)

    return [-1]


def get_all_directions_dots(x, y):
    return [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

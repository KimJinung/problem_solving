"""
활용할 배열을 미리 만들어두고 풀이하는 방법

반드시 한 번 더 풀어볼 것
"""


def solution(n):
    snail = []

    for i in range(1, n + 1):
        snail.append([0 for _ in range(i)])

    number = 0

    row, col = -1, 0

    for i in range(n, 0, -3):
        for _ in range(i):
            row += 1
            number += 1
            snail[row][col] = number
        for _ in range(i - 1):
            col += 1
            number += 1
            snail[row][col] = number
        for _ in range(i - 2):
            row -= 1
            col -= 1
            number += 1
            snail[row][col] = number

    return [num for subset in snail for num in subset]

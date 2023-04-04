import math


def solution(n):
    value = math.sqrt(n)

    if value % 1 == 0:
        return (value + 1) ** 2

    return -1

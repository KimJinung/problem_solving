def solution(n):
    value = 1
    repeat = 0

    while value <= n:
        repeat += 1
        value *= repeat

    return repeat - 1

def solution(a, b):
    return max(sum_by_string(a, b), sum_by_string(b, a))


def sum_by_string(num1: int, num2: int) -> int:
    return int(str(num1) + str(num2))

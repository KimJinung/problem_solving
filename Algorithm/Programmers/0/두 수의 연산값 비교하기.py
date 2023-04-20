def solution(a, b):
    return max(add_by_string(a, b), 2 * a * b)


def add_by_string(a: int, b: int) -> int:
    return int(str(a) + str(b))

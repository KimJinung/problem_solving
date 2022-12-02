def solution(brown, yellow):
    divisor_pair = get_divisor_pair(brown + yellow)

    for col, row in divisor_pair:
        if row == 1:
            continue

        border_line = (col * 2) + ((row - 2) * 2)

        if brown == border_line and col * row - border_line == yellow:
            return [col, row]


def get_divisor_pair(num: int) -> list:
    result = []

    for n in range(1, int(num**0.5) + 1):
        if num % n == 0:
            result.append([num // n, n])

    return result

def solution(n, left, right):
    result = []

    for num in range(left, right + 1):
        x = num % n
        y = num // n

        result.append(max(x, y) + 1)

    return result

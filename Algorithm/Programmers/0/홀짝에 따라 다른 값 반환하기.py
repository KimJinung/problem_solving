def solution(n):
    if n % 2 != 0:
        return sum(num for num in range(1, n + 1, 2))

    return sum(num**2 for num in range(2, n + 1, 2))

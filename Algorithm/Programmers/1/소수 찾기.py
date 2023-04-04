import math


def solution(n):
    return len([num for num in range(2, n + 1) if is_prime(num)])


def is_prime(num: int) -> bool:
    for divisor in range(2, int(math.sqrt(num) + 1)):
        if num % divisor == 0:
            return False

    return True

from math import sqrt
from itertools import combinations


def solution(nums):
    answer = 0

    combi = list(combinations(nums, 3))

    for numbers in combi:
        if is_prime(sum(numbers)):
            answer += 1

    return answer


def is_prime(number: int) -> bool:
    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True

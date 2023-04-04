import math


def solution(arr):
    answer = arr[0]

    for idx in range(1, len(arr)):
        answer = lcm(answer, arr[idx])

    return answer


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

import math


def solution(n, m):
    gcd = math.gcd(n, m)

    return [gcd, n * m / gcd]

import math

def solution(n):
    return (6 * n / math.gcd(6, n)) // 6

    # python >= 3.9 
    # return math.lcm(6, n) // 6
def solution(n, k):
    service = n // 10 * 2000
    return n * 12000 + 2000 * k - service
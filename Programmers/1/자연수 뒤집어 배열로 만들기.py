def solution(n):
    return list(map(lambda x: int(x), list(str(n))))[::-1]

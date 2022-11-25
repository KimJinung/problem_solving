def solution(sizes):
    return max(max(n) for n in sizes) * max(min(n) for n in sizes)

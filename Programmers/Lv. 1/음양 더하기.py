def solution(absolutes, signs):
    return sum(num if signs[idx] else -num for idx, num in enumerate(absolutes))

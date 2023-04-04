def solution(numbers, k):
    idx = (k - 1) * 2 % len(numbers)
    return numbers[idx]

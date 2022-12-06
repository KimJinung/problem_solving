from collections import Counter
from functools import reduce


def solution(clothes):
    clothes = [item[1] for item in clothes]

    s = Counter(clothes)

    number_of_cases = list(s.values())

    return reduce(lambda x, y: x * (y + 1), number_of_cases, 1) - 1

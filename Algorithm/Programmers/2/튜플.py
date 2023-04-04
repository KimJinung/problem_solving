import re
from collections import Counter


def solution(s):
    s = Counter(re.findall("[\d]+", s))

    return list(map(int, sorted(s, key=s.get, reverse=True)))

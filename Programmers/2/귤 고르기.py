from collections import Counter


def solution(k, tangerine):
    answer = 0

    tangerine_dict = Counter(tangerine)

    weights = sorted(tangerine_dict.values(), reverse=True)

    for weight in weights:
        k -= weight
        answer += 1

        if k <= 0:
            return answer

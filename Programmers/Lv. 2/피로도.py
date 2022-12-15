from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for case in permutations(dungeons):
        current_k = k
        count = 0

        for need_tiredness, tiredness in case:
            if current_k >= need_tiredness and current_k - tiredness >= 0:
                current_k -= tiredness
                count += 1
            else:
                break

        answer = max(answer, count)

    return answer

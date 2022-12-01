def solution(k, score):
    scores = score
    k -= 1

    answer = []

    award = []

    for idx, score in enumerate(scores):
        award.append(score)
        award.sort(reverse=True)

        if idx < k:
            answer.append(award[-1])
        else:
            answer.append(award[k])

    return answer

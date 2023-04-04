def solution(k, m, score):
    answer = 0

    score.sort()

    length = len(score)

    start_point = length % m

    while start_point < length:
        answer += score[start_point] * m
        start_point += m

    return answer

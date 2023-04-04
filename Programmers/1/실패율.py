def solution(N, stages):
    answer = {}

    denominator = len(stages)

    for stage in range(1, N + 1):
        if not denominator:
            answer[stage] = 0
        else:
            numerator = stages.count(stage)

            answer[stage] = numerator / denominator

            denominator -= numerator

    return sorted(answer, key=lambda x: -answer[x])

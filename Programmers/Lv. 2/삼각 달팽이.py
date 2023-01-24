def solution(n):
    answer = [[] for _ in range(n)]

    size = sum(i for i in range(1, n + 1))

    snail = []
    tmp_snail = []

    step = n

    for num in range(1, size + 1):
        tmp_snail.append(num)

        if len(tmp_snail) == step:
            snail.append(tmp_snail)
            tmp_snail = []
            step -= 1

    idx = -1

    for direction, subset in enumerate(snail):
        if direction % 3 == 0:
            for num in subset:
                idx += 1
                answer[idx].insert(-1, num)
        elif direction % 3 == 1:
            for num in subset:
                answer[idx].insert(-1, num)
        elif direction % 3 == 2:
            for num in subset:
                idx -= 1
                answer[idx].insert(-1, num)

    return [num for subset in answer for num in subset]

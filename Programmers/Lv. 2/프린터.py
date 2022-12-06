def solution(priorities, location):
    answer = 1

    queue = [(weight, idx) for idx, weight in enumerate(priorities)]

    while queue:
        next_document = max(queue, key=lambda x: x[0])

        if queue[0][1] == location:
            return answer

        if queue[0] != next_document:
            start_idx = queue.index(next_document)

            queue = queue[start_idx:] + queue[:start_idx]

        del queue[0]

        answer += 1

    return answer

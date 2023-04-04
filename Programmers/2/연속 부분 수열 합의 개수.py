def solution(elements):
    answer = set()

    size = len(elements)

    elements *= 2

    for window_size in range(1, size + 1):
        for start_idx in range(size):
            value = sum(elements[start_idx : start_idx + window_size])

            answer.add(value)

    return len(answer)

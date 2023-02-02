def solution(triangle):
    triangle = triangle[::-1]

    for depth, subset in enumerate(triangle):
        if depth == 0:
            continue

        for idx, num in enumerate(subset):
            update_value = max(
                num + triangle[depth - 1][idx], num + triangle[depth - 1][idx + 1]
            )

            triangle[depth][idx] = update_value

    return triangle[-1][0]

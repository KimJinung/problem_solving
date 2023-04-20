def solution(a, d, included):
    size = len(included)

    arr = [
        integer
        for idx, integer in enumerate(range(a, a + d * size, d))
        if included[idx]
    ]

    return sum(arr)

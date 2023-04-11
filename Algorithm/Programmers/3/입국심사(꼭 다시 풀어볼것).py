def solution(n, times):
    min_time = min(times)

    right = min_time * n
    left = min_time

    while left + 1 != right:
        mid = (left + right) // 2

        workload = sum(mid // t for t in times)

        if workload >= n:
            right = mid
        else:
            left = mid

    return right
def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum([A[idx] * B[idx] for idx, _ in enumerate(A)])

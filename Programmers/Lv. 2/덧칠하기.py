from collections import deque


def solution(n, m, section):
    answer = 0

    Q = deque(section)

    while Q:
        wall = Q.popleft()

        while Q and Q[0] < wall + m:
            Q.popleft()

        answer += 1

    return answer

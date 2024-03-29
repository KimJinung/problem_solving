from collections import deque


def solution(x, y, n):
    discoverd = {}

    Q = deque([(x, 0)])

    while Q:
        num, depth = Q.popleft()

        if num == y:
            return depth

        if not discoverd.get(num):
            discoverd[num] = True

            for next_num in [num * 3, num * 2, num + n]:
                if next_num <= y:
                    Q.append((next_num, depth + 1))

    return -1

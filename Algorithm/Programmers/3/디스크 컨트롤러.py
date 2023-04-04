"""
문제가 요구하는 것
- 특정 시점에서 작업량이 가장 작은 케이스를 추출

사용할 알고리즘
- 힙

아이디어
- 시간을 체크한다.
- 현재 시점에서 작업 가능한 케이스를 모두 힙에 넣는다.
- 힙에서 가장 작업량이 작은 디스크를 가져와서 작업한다.
- 작업한 디스크의 시간만큼 업데이트 한다.
"""
import heapq


def solution(jobs):
    answer = 0

    stack = sorted(jobs, key=lambda x: x[0], reverse=True)
    Q = []

    current_time = 0

    while stack or Q:
        while stack and stack[-1][0] <= current_time:
            start, work = stack.pop()

            heapq.heappush(Q, [work, start])

        if Q:
            work, start = heapq.heappop(Q)

            answer += work + current_time - start

            current_time += work
        else:
            current_time += 1

    return answer // len(jobs)

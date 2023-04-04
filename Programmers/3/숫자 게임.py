"""
문제가 요구하는 것
- 최대한 작은 수로 상대방에게 이기는 것

사용할 알고리즘
- 힙

아이디어
- A팀 배열을 정렬한다.
- B팀 배열에서 가장 작은 값을 가져온다.
    - 해당 숫자가 A팀의 가장 작은 숫자보다 크다면 승리
    - 해당 숫자가 A팀의 가장 작은 숫자보다 작다면 패배이므로 다음숫자로 재대결 시킨다.

*풀고 보니까 굳이 힙을 안쓰고 정렬만 사용해도 가능할 듯하다.
"""


import heapq
from collections import deque


def solution(A, B):
    answer = 0

    A = deque(sorted(A))

    heapq.heapify(B)

    num_of_A = A.popleft()

    while A and B:
        num_of_B = heapq.heappop(B)

        if num_of_B > num_of_A:
            answer += 1

            num_of_A = A.popleft()

    if B:
        answer += 1

    return answer

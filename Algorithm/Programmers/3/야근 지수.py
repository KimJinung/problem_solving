"""
문제에서 요구하는 것
- works 배열에서 n만큼 제거했을 때 제곱의 합이 가장 작은 케이스
- 최고의 집합 문제와 비슷하지만 이 문제는 works의 인자가 주어진 것보다 커질 수 없다는 제약조건이 있음


문제 접근 방법
1. 내림 차순 정렬
2. 가장 큰 값이 두 번째 큰 값보다 작아질 때까지 뺀다. (0번 인덱스가 1번 인덱스보다 작아질 때까지)
3. 2번 케이스가 완료되면 0번째 인덱스보다 큰 값이 사라질때까지 뺀다.
4. 2~3번 반복

*과정 중 n이 0이 되면 종료한다.


아쉬운 점
- 처음에 정렬을 쓰지 않고 접근하는 방법이 없을까?
* 힙을 사용한 풀이 추가
"""


def solution(n, works):
    if sum(works) < n:
        return 0

    size = len(works)

    works.sort(reverse=True)

    while n != 0:
        if works[0] >= works[1]:
            works[0] -= 1

            n -= 1
        else:
            for idx in range(1, size):
                if works[idx] > works[0]:
                    works[idx] -= 1

                    n -= 1

                    if not n:
                        break

    return sum(map(lambda x: x**2, works))


"""
힙을 사용한 풀이
"""

import heapq


def solution2(n, works):
    if sum(works) < n:
        return 0

    works = list(map(lambda x: -x, works))

    heapq.heapify(works)

    while n != 0:
        value = heapq.heappop(works)

        heapq.heappush(works, value + 1)

        n -= 1

    return sum(map(lambda x: (-x) ** 2, works))

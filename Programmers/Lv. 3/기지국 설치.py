"""
문제가 요구하는 것
- 기지국을 최소로 설치하는 방법
- 주어진 숫자 범위를 이용해서 배열을 가능한 많이 채우는 방법


사용할 알고리즘
- 그리디


아이디어
- 기지국 배열을 이용해서 전파가 닿지 않는 영역만 체크한다.
"""

from math import ceil


def solution(n, stations, w):
    answer = 0

    remaining_area = []

    head = 1

    for station in stations:
        tail = station - w

        if tail - head > 0:
            remaining_area.append(tail - head)

        head = station + w + 1

    if head <= n:
        remaining_area.append(n - head + 1)

    for area in remaining_area:
        answer += ceil(area / (w * 2 + 1))

    return answer

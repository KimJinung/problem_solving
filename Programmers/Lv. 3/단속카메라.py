"""
문제가 요구하는 것
- 배열에서 요소가 겹치는 지점의 개수


아이디어
- 카메라가 항상 진출 시점에 설치되어야 효율적이다.
- 진출 시점을 오름차순으로 정렬한다.
- 배열을 순회하면서 해당 인자의 진입 시점이 이전 인자의 진출 시점 이전인지 확인한다.
"""


def solution(routes):
    answer = 1

    routes.sort(key=lambda x: x[1])

    cam = routes[0][1]

    for idx in range(1, len(routes)):
        start_line = routes[idx][0]

        if start_line > cam:
            answer += 1

            cam = routes[idx][1]

    return answer

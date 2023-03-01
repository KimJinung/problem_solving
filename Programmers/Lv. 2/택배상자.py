"""
문제가 요구하는 것
- 특정 시점에 두 개의 자료 구조에서 순차적으로 필요한 인자가 확인하는 것

사용할 자료 구조
- 큐
- 스택

아이디어
- 우선적으로 서브 컨테이너 벨트(스택)의 마지막 인자가 택배 번호와 일치하면 제거한다.
- 그렇지 않으면 컨테이너 벨트(큐)의 첫 번째 인자가 순번과 일치하면 그대로 제거한다.
- 위 두 가지 케이스 어디에도 해당하지 않으면 컨테이너 벨트의 첫 번째 인자를 서브 컨테이너 벨트에 삽입한다.
- 위 과정을 반복하면서 서브 컨테이너에서도 필요한 택배를 찾지 못하고, 컨테이너 벨트에 아무런 인자도 없으면 종료
"""
from collections import deque


def solution(order):
    answer = 0

    order = deque(order)
    container_belt = deque([n for n in range(1, len(order) + 1)])
    sub_container_belt = []

    while container_belt or sub_container_belt:
        target_package = order[0]

        if sub_container_belt and sub_container_belt[-1] == target_package:
            sub_container_belt.pop()
            order.popleft()
            answer += 1
        elif container_belt and container_belt[0] == target_package:
            container_belt.popleft()
            order.popleft()
            answer += 1
        elif not container_belt:
            break
        else:
            package = container_belt.popleft()
            sub_container_belt.append(package)

    return answer

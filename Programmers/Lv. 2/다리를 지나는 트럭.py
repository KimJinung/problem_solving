"""
1. while loop 한 번을 1초라고 가정한다.
2. 대기 큐에 트럭이 존재하고, 다리에 해당 트럭을 올려도 무게를 초과하지 않으면 다리 큐에 추가 한다.
3. 다리 큐의 모든 트럭들이 가진 시간이 감소한다.
4. 다리 큐에 제일 먼저 들어온 트럭의 시간이 0이 되면 디 큐
5. 1~4 과정을 대기 큐와 다리 큐에 트럭이 없을 때까지 반복한다.
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    waitting_q = deque(truck_weights)
    bridge_q = deque()

    while waitting_q or bridge_q:  # case 1, 5
        answer += 1

        if (  # case 2
            waitting_q
            and sum(weight for weight, _ in bridge_q) + waitting_q[0] <= weight
        ):
            truck = waitting_q.popleft()

            bridge_q.append([truck, bridge_length])

        for idx in range(len(bridge_q)):  # case 3
            bridge_q[idx][1] -= 1

        if bridge_q[0][1] == 0:  # case 4
            bridge_q.popleft()

    return answer + 1

"""
문제가 요구하는 것
- A, B경로까지 최소 합승 요금
- 동승하지 않는 경우가 최소인 경우도 가능하다.

사용할 알고리즘
- 다익스트라

아이디어
1. 모든 지점을 첫 번째 하차 지점이라고 가정하고 출발 지점부터 해당 지점까지의 최단거리를 구한다. 
2. 위 하차 지점에서 A, B까지의 최단거리를 구한다.

1번과 2번의 합이 최소가 되는 것이 정답
"""
from collections import defaultdict

import heapq


def solution(n, s, a, b, fares):
    answer = float("inf")

    graph = defaultdict(list)

    for departure, arrival, weight in fares:
        graph[departure].append((weight, arrival))
        graph[arrival].append((weight, departure))

    def _dijkstra(start: int) -> dict:
        distance_history = {node: float("inf") for node in range(1, n + 1)}

        Q = [(0, start)]

        while Q:
            weight, node = heapq.heappop(Q)

            if weight < distance_history[node]:
                distance_history[node] = weight

                for next_weight, next_node in graph[node]:
                    heapq.heappush(Q, (weight + next_weight, next_node))

        return distance_history

    distance_history = _dijkstra(s)

    for node, weight in distance_history.items():
        sub_weight_history = _dijkstra(node)

        value_of_a = sub_weight_history[a]
        value_of_b = sub_weight_history[b]

        result = weight + value_of_a + value_of_b

        if result < answer:
            answer = result

    return answer

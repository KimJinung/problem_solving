"""
문제가 요구하는 것
- 그래프의 최단 거리

사용할 알고리즘
- Dijkstra

주의사항
- 노드에서 단일 방향 진해잉 아닌, 양방향 그래프
"""

import heapq


def solution(N, road, K):
    graph = {n: [] for n in range(1, N + 1)}

    dist = {}

    # Make graph
    for start, end, weight in road:
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    # Dijkstra
    queue = [(0, 1)]

    while queue:
        weight, node = heapq.heappop(queue)

        if node not in dist:
            dist[node] = weight

            for v, w in graph[node]:
                new_weight = weight + w
                heapq.heappush(queue, (new_weight, v))

    return len([value for value in dist.values() if value <= K])

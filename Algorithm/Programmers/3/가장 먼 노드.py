"""
문제가 요구하는 것
- 가장 멀리 떨어진 노드의 개수
*즉 최단거리 구해서 가장 긴 노선의 개수를 구하라는 의미


사용할 알고리즘
- Dijkstra
"""


from collections import defaultdict
import heapq


def solution(n, edge):
    graph = defaultdict(list)

    # Make graph
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    # Dijkstra
    distance = get_distance_counts(graph, n)

    max_distance = max(distance)

    return distance.count(max_distance)


def get_distance_counts(graph: dict, size: int):
    distance = []

    discoverd = {n: False for n in range(1, size + 1)}

    Q = [[0, 1]]
    heapq.heapify(Q)

    while Q:
        depth, node = heapq.heappop(Q)

        if not discoverd[node]:
            discoverd[node] = True
            distance.append(depth)

            for next_node in graph[node]:
                heapq.heappush(Q, [depth + 1, next_node])

    return distance

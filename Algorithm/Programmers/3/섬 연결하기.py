"""
문제가 요구하는 것
- 그래프의 최단 거리

사용할 알고리즘
- Dijkstra
"""


from collections import defaultdict
import heapq


def solution(n, costs):
    # Make graph
    graph = defaultdict(list)

    for start, end, cost in costs:
        graph[start].append([cost, end])
        graph[end].append([cost, start])

    # Dijkstra
    cost = get_costs(graph, n)

    return sum(cost)


def get_costs(graph: dict, size: int) -> list:
    costs = []
    discoverd = {n: False for n in range(size)}
    discoverd[0] = True

    Q = graph[0]
    heapq.heapify(Q)

    while Q:
        cost, node = heapq.heappop(Q)

        if not discoverd[node]:
            discoverd[node] = True
            costs.append(cost)

            for cost, next_node in graph[node]:
                heapq.heappush(Q, [cost, next_node])

    return costs

"""
문제가 요구하는 것
- 그래프 그룹의 개수

사용할 알고리즘
- DFS
"""

from collections import defaultdict


def solution(n, computers):
    answer = 0

    # Make graph
    graph = defaultdict(list)

    for current_idx, networks in enumerate(computers):
        for network_idx, network in enumerate(networks):
            if current_idx != network_idx and network:
                graph[current_idx + 1].append(network_idx + 1)

    # DFS
    discoverd = {n: False for n in range(1, n + 1)}

    def dfs(start_node: int, graph: dict):
        stack = [start_node]

        while stack:
            node = stack.pop()

            if not discoverd[node]:
                discoverd[node] = True

                for next_node in graph[node]:
                    stack.append(next_node)

    # Check network group
    for num in range(1, n + 1):
        if not discoverd[num]:
            dfs(num, graph)

            answer += 1

    return answer

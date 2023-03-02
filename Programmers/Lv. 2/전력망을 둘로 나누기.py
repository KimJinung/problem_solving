"""
1. wires를 하나 누락 시켜서 트리 생성
    1-1. 1부터 dfs 태워서 개수 검사 + 방문 체크
    1-2. 방문 안한 다음 노드 개수 검사해서 차이 확인
"""

from collections import defaultdict


def solution(n, wires):
    answer = -1

    for exclude_number in range(len(wires)):
        tree_items = wires[:exclude_number] + wires[exclude_number + 1 :]

        graph = defaultdict(list)

        for _from, _to in tree_items:
            graph[_from].append(_to)
            graph[_to].append(_from)

        result = []

        for num in range(1, n + 1):
            cnt = dfs(num, n, graph)
            result.append(cnt)

        diff = max(result) - min(result)

        if answer and answer > diff:
            answer = diff
        elif answer == -1:
            answer = diff

    return answer


def dfs(start: int, node_size: int, graph: dict):
    result = 0

    discoverd = {n: False for n in range(1, node_size + 1)}

    stack = [start]

    while stack:
        node = stack.pop()

        if not discoverd[node]:
            discoverd[node] = True
            result += 1

            for next_node in graph[node]:
                stack.append(next_node)

    return result

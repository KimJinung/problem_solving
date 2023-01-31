"""
문제가 요구하는 것
- 최단 거리

사용할 알고리즘
- BFS

아이디어
- 알파벳이 하나씩 다른 단어끼리 양방향 그래프 생성
"""

from collections import defaultdict, deque


def solution(begin, target, words):
    answer = 0

    # Make graph
    graph = defaultdict(set)

    for word1 in words:
        for word2 in words:
            if diff_ch_count_between_str(word1, word2) == 1:
                graph[word1].add(word2)
                graph[word2].add(word1)

    # Business logic
    for word in words:
        if diff_ch_count_between_str(begin, word) == 1:
            result = bfs(word, graph, target)

            if not answer:
                answer = result
            elif result < answer:
                answer = result

    return answer


def diff_ch_count_between_str(str1: str, str2: str):
    diff = 0

    for idx in range(len(str1)):
        if str1[idx] != str2[idx]:
            diff += 1

    return diff


def bfs(start_node: int, graph: dict, target: str) -> int:
    discoverd = []

    queue = [(start_node, 1)]

    queue = deque(queue)

    while queue:
        node, depth = queue.popleft()

        if node == target:
            return depth

        if node not in discoverd:
            discoverd.append(node)

            for next_node in graph[node]:
                queue.append((next_node, depth + 1))

    return 0

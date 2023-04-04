"""
재귀를 이용한 풀이

1. DFS가 항상 depth를 우선으로 탐색하는 것을 응용하는 방법이다.
2. 현재 탐색 중인 depth와 누적합을 확인하여 카운팅한다.
"""


def solution(numbers, target):
    answer = 0

    def recursive_dfs(depth: int, total: int):
        if depth == len(numbers):
            if total == target:
                nonlocal answer

                answer += 1

            return

        recursive_dfs(depth + 1, total + numbers[depth])
        recursive_dfs(depth + 1, total - numbers[depth])

    recursive_dfs(0, 0)

    return answer


"""
스택을 활용한 풀이

1. 스택이 비기 전까지 루프를 반복한다.
    1-1. 마지막 노드를 가져온다
    1-2. 마지막 노드에서 다음 2가지 케이스를 만들고 큐에 넣는다.
    1-3. depth가 limit에 걸린 경우 새로운 케이스를 추가하지 않고 검사만 한다.
"""


def solution2(numbers, target):
    answer = 0

    que = [[0, 0]]

    while len(que) > 0:
        index, node = que.pop()

        if index < len(numbers):
            que.append([index + 1, node + numbers[index]])
            que.append([index + 1, node - numbers[index]])

        if index == len(numbers):
            if node == target:
                answer += 1

    return answer

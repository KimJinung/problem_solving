"""
문제가 요구하는 것
- 주어진 항공권을 모두 사용해서 전체 경로를 모두 탐색한다.
- 단 모든 도시를 방문하지 못하는 경우는 없다.


사용할 알고리즘
- DFS
- 경로 탐색을 무한 반복 하게 되는 경우, 그리고 더이상 경로를 탐색하지 못하는 경우 종료한다.


아이디어
- 경로를 잘못 진입해서 끝까지 탐색하지 못하는 경우가 발생할 수 있다. <- 이 경우를 예측할 수 없다.
- 따라서 그래프 경로마다 모두 탐색하되 티켓 사이즈를 넘어가는 경우, 무한 루프에 빠진 것이므로 탐색을 종료한다.
- 티켓 히스토리를 매 재귀마다 넘겨주어서 티켓이 있는 곳만 경유한다.
- 티켓을 정확히 사용해서 모두 개수가 0개이고 route 사이즈가 max route size와 일치하는 경우는 정답이 될 수 있다.

*티켓이 3개인 경우 총 4곳을 거치게 되고, 티켓이 5개인 경우 총 6곳을 경유한다. (티켓 개수 + 1이 route의 사이즈가 된다.)

복기
*문제를 제대로 이해하지 못해서 오랜 시간을 소요한 문제
항상 문제를 정확히 이해하고, 로직을 정확히 작성하고 코드 작성을 시작하자.
"""
from collections import defaultdict


def solution(tickets):
    answer = []

    max_route_size = len(tickets) + 1

    graph = defaultdict(list)

    ticket_history = defaultdict(int)

    for _from, _to in tickets:
        graph[_from].append(_to)
        ticket_history[(_from, _to)] += 1

    def _recursive_dfs(route: list, depth: int, ticket_history: dict) -> None:
        route_size = len(route)

        if route_size > max_route_size:
            return

        if not all(ticket_history.values()) and route_size == max_route_size:
            answer.append(route)
            return

        last_airport = route[-1]

        for next_airport in graph[last_airport]:
            if ticket_history[(last_airport, next_airport)]:
                updated_ticket_history = ticket_history.copy()

                updated_ticket_history[(last_airport, next_airport)] -= 1

                _recursive_dfs(
                    route + [next_airport], depth + 1, updated_ticket_history
                )

    _recursive_dfs(["ICN"], 1, ticket_history)

    return sorted(answer)[0]

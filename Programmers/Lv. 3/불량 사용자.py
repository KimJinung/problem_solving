"""
문제가 요구하는 것
- 가능한 경우의 수


사용할 알고리즘
- 재귀


아이디어
- 가능한 케이스를 모두 만든다.
- 다음 가능한 케이스에서 중복 가능한 케이스만 거른다.
- 위 패턴이 동일하게 반복된다 -> 그래프 형태를 띄게 된다. -> 재귀로 탐색한다.
"""


def solution(user_id, banned_id):
    answer = []

    user_id_list = user_id
    banned_id_list = banned_id

    # Make number of case
    cases = []

    for banned_id in banned_id_list:
        case = []

        for user_id in user_id_list:
            if is_matched_user_id(user_id, banned_id):
                case.append(user_id)

        cases.append(case)

    # Remove duplicated case
    def recursive(route: list, depth: int):
        if depth == len(banned_id_list):
            route.sort()

            if route not in answer:
                answer.append(route)

            return

        for uid in cases[depth]:
            if uid not in route:
                recursive(route + [uid], depth + 1)

    recursive([], 0)

    return len(answer)


def is_matched_user_id(user_id: str, banned_id: str) -> bool:
    user_id_size = len(user_id)
    banned_id_size = len(banned_id)

    if user_id_size != banned_id_size:
        return False

    for idx in range(user_id_size):
        if banned_id[idx] == "*":
            continue

        if user_id[idx] != banned_id[idx]:
            return False

    return True

def solution(n, a, b):
    answer = 0

    while a != b:
        a = get_current_group_number(a)
        b = get_current_group_number(b)

        answer += 1

    return answer


def get_current_group_number(number: int) -> int:
    if number % 2 != 0:
        number += 1

    return number // 2

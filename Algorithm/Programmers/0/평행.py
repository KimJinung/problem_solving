def solution(dots):
    answer = 0

    number_of_case = [[(0, 1), (2, 3)], [(0, 2), (1, 3)], [(0, 3), (1, 2)]]

    for case in number_of_case:
        first = calcul_dot(dots[case[0][0]], dots[case[0][1]])
        second = calcul_dot(dots[case[1][0]], dots[case[1][1]])

        if is_parallel(first, second):
            return 1

    return answer


def calcul_dot(dot1: list, dot2: list) -> list:
    x = dot1[0] - dot2[0]
    y = dot1[1] - dot2[1]

    return [abs(x), abs(y)]


def is_parallel(first: list, second: list) -> bool:
    return first[1] / first[0] == second[1] / second[0]

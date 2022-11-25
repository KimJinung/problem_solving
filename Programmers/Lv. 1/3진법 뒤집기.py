def solution(n):
    value = get_ternary(n)

    return int(value, 3)


def get_ternary(num: int):
    answer = ""

    while num != 0:
        value = num // 3
        mod = num % 3

        num = value
        answer += str(mod)

    return answer

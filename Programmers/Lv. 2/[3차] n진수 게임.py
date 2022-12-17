"""
*진수 변환 시 10진법이 넘는 경우에만 문자열 처리가 필요하다.
"""


def solution(n, t, m, p):
    result = "0"

    for num in range(1, t * m):
        result += get_radix(n, num)

    return "".join(result[idx] for idx in range(p - 1, t * m, m))


def get_radix(n: int, number: int) -> str:
    result = ""

    while number != 0:
        number, mod = divmod(number, n)

        if n > 10 and (10 <= mod <= 15):
            result += "ABCDEF"[mod % 10]
        else:
            result += str(mod)

    return result[::-1]

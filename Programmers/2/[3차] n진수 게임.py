"""
*진수 변환 시 10진법이 넘는 경우에만 문자열 처리가 필요하다.
"""


def solution(n, t, m, p):
    result = "0"

    for num in range(1, t * m):
        result += radix_transformation(n, num)

    return "".join(result[idx] for idx in range(p - 1, t * m, m))


def radix_transformation(base: int, number: int) -> str:
    result = ""

    while number != 0:
        number, mod = divmod(number, base)

        if base > 10 and (10 <= mod <= 15):
            result += "ABCDEF"[mod % 10]
        else:
            result += str(mod)

    return result[::-1]

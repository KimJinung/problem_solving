def solution(number, limit, power):
    answer = 0

    for knight in range(1, number + 1):
        divisor_count = get_divisor(knight)

        if divisor_count > limit:
            divisor_count = power

        answer += divisor_count

    return answer


def get_divisor(num: int) -> int:
    result = 0

    for n in range(1, int(num ** (1 / 2)) + 1):
        if num % n == 0:
            result += 1

            if n != (num // n):
                result += 1

    return result

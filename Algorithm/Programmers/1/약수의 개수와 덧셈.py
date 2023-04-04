def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        divisor = get_divisor_count(num)

        if divisor % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer


def get_divisor_count(num: int) -> int:
    result = 0

    for i in range(1, num + 1):
        if num % i == 0:
            result += 1

    return result

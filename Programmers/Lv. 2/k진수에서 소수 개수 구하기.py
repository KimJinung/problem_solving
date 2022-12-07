import re


def solution(n, k):
    answer = 0

    digits = get_n_number(n, k)

    preprocessed_digits = re.findall("[1-9]+", digits)

    for digit in preprocessed_digits:
        if is_prime(int(digit)):
            answer += 1

    return answer


def get_n_number(n, k):
    result = ""

    while n != 0:
        mod = n % k
        n = n // k

        result += str(mod)

    return result[::-1]


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

from itertools import permutations


def solution(numbers):
    answer = 0

    number_of_case = set()

    for size in range(1, len(numbers) + 1):
        case = map(int, map("".join, permutations(list(numbers), size)))

        number_of_case.update(case)

    for num in number_of_case:
        if is_prime(int(num)):
            answer += 1

    return answer


def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for divisor in range(2, int(number**1 / 2) + 1):
        if number % divisor == 0:
            return False

    return True

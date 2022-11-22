from fractions import Fraction


def solution(a, b):
    fraction = Fraction(a, b)

    denom = fraction.denominator

    for num in range(3, denom + 1):
        if num != 5 and denom % num == 0 and is_prime(num):
            return 2

    return 1


def is_prime(number: int) -> bool:
    for num in range(2, number):
        if number % num == 0:
            return False

    return True

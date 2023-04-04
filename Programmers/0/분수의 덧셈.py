from fractions import Fraction


def solution(denum1, num1, denum2, num2):
    result = Fraction(denum1, num1) + Fraction(denum2, num2)

    return [result.numerator, result.denominator]

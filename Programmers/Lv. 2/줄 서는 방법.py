from math import factorial


def solution(n, k):
    answer = []

    numbers = [num for num in range(1, n + 1)]

    while k != 0 and k != 1:
        n_factorial = factorial(n - 1)

        quotient, remainder = divmod(k, n_factorial)

        if remainder == 0:
            quotient -= 1

        value = numbers.pop(quotient)

        answer.append(value)

        k = remainder
        n -= 1

    if k == 0:
        numbers.sort(reverse=True)
    elif k == 1:
        numbers.sort()

    return answer + numbers


"""
숫자가 생성되는 패턴
[1, 2, 3, 4]의 경우 
[1] + [2, 3, 4]
[2] + [1, 3, 4]

위처럼 prefix + 경우의 수 개수가 된다
4의 경우는 4가지 케이스에 각각 6! 케이스가 가능하다.
이러한 패턴이 자릿수마다 반복된다. 
(다음 k는 나머지에 해당하고, 자릿수가 줄어든다.)

*remainder가 0이면 quotient를 1빼주어야함
"""

def solution(n, s):
    if n > s:
        return [-1]

    answer = []

    while n != 0:
        quotient = s // n

        answer.append(quotient)

        s -= quotient

        n -= 1

    return answer

def solution(n):
    answer = 0

    while n != 0:
        if n % 2 != 0:
            answer += 1
            n -= 1

        n //= 2

    return answer


# 2진법을 이용한 풀이
def solution2(n):
    return bin(n).count("1")

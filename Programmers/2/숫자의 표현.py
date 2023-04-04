def solution(n):
    answer = 0

    mem = []

    for x in range(1, n + 1):
        mem = []

        for y in range(x, n + 1):
            mem.append(y)

            if sum(mem) == n:
                answer += 1
                break

            if sum(mem) > n:
                break

    return answer


# 수학을 이용한 풀이
def solution(n):
    return len([i for i in range(1, n + 1, 2) if n % i == 0])

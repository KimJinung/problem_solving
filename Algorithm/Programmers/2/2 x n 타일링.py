def solution(n):
    answer = 2
    prev = 1

    for _ in range(3, n + 1):
        tmp = answer
        answer += prev
        prev = tmp

    return answer % 1000000007 if answer > 1 else 1

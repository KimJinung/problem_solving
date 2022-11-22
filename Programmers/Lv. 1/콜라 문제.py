def solution(a, b, n):
    answer = 0

    fee = a
    reward = b
    current_empty_bottle = n

    while current_empty_bottle // fee > 0:
        value = current_empty_bottle // fee * reward
        mod = current_empty_bottle % fee

        answer += value
        current_empty_bottle = mod + value

    return answer

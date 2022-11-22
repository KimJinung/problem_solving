def solution(my_str, n):
    answer = []

    for idx in range(0, len(my_str), n):
        answer.append(my_str[idx : idx + n])

    return answer

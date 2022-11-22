def solution(i, j, k):
    answer = 0

    target = str(k)

    for num in range(i, j + 1):
        str_num = str(num)

        if target in str_num:
            answer += str_num.count(target)

    return answer

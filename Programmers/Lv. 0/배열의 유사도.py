def solution(s1, s2):
    answer = 0

    s1_dict = {key: True for key in s1}

    for key in s2:
        if s1_dict.get(key):
            answer += 1

    return answer

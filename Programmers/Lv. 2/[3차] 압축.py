"""
1. 사전에 존재하는 최장 문자열을 어떻게 확인할 것인지가 포인트
    - W+C가 사전에 존재하지 않는 경우까지 탐색
    - 위 경우 W가 최장 문자열에 해당
    
"""
import string


def solution(msg):
    answer = []

    dic = {letter: idx + 1 for idx, letter in enumerate(string.ascii_uppercase)}

    last_idx = 27

    msg = ["exit"] + list(msg)[::-1]

    W = msg.pop()

    while W != "exit":
        C = msg.pop()

        if dic.get(W + C):
            W = W + C
        else:
            answer.append(dic.get(W))

            dic[W + C] = last_idx

            last_idx += 1

            W = C

    return answer

def solution(s):
    answer = [0, 0]

    while s != "1":
        answer[1] += s.count("0")
        answer[0] += 1

        next_s = len(s.replace("0", ""))

        s = bin(next_s)[2:]

    return answer

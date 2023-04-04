def solution(s):
    answer = []

    for item in s.split():
        if item == "Z":
            if len(answer) >= 1:
                answer.pop()
        else:
            answer.append(int(item))

    return sum(answer)

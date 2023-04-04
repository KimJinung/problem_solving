def solution(lines):
    answer = 0

    arr = [0] * 200

    for line in lines:
        for dot in range(line[0], line[1]):
            arr[dot + 100] += 1

    for item in arr:
        if item >= 2:
            answer += 1

    return answer

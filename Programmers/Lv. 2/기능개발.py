def solution(progresses, speeds):
    answer = []

    progresses = progresses[::-1]
    speeds = speeds[::-1]

    while progresses:
        progresses = [p + speeds[idx] for idx, p in enumerate(progresses)]

        result = 0

        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()

            result += 1

        if result:
            answer.append(result)

    return answer

import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

length = len(lower)


def solution(s, n):
    answer = ""

    for ch in s:
        if ch == " ":
            answer += " "
            continue

        if ch.islower():
            idx = lower.index(ch)

            answer += lower[(idx + n) % length]
        else:
            idx = upper.index(ch)

            answer += upper[(idx + n) % length]

    return answer
